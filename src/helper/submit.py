import argparse
import sys

from colorist import Color
from index_now import (DaysAgo, IndexNowAuthentication, SearchEngineEndpoint,
                       SitemapFilter, submit_sitemaps_to_index_now,
                       submit_urls_to_index_now)

SUCCESS_STATUS_CODES = [200, 202, 204]


def is_successful_response(status_code: int) -> bool:
    return status_code in SUCCESS_STATUS_CODES


def exit_with_success() -> None:
    sys.exit(0)


def exit_with_failure() -> None:
    sys.exit(1)


def get_endpoint_from_input(endpoint: str) -> SearchEngineEndpoint:
    """Get a search engine endpoint from text input.

    Args:
        endpoint (str): Input from CLI parameter, e.g `"indexnow"`, `"bing"`, `"naver"`, `"seznam"`, `"yandex"`, `"yep"`.

    Returns:
        SearchEngineEndpoint: Search engine endpoint. Fallback is Microsoft Bing.
    """

    match str(endpoint).lower():
        case "indexnow":
            return SearchEngineEndpoint.INDEXNOW
        case "bing":
            return SearchEngineEndpoint.BING
        case "naver":
            return SearchEngineEndpoint.NAVER
        case "seznam":
            return SearchEngineEndpoint.SEZNAM
        case "yandex":
            return SearchEngineEndpoint.YANDEX
        case "yep":
            return SearchEngineEndpoint.YEP
        case _:
            return SearchEngineEndpoint.BING


def normalise_string(input: str) -> str:
    """Normalize the input string by removing any single or double quotes as well as trimming any whitespace."""

    return input.replace('"', "").replace("'", "").strip()


def parse_string_or_list_input(string_or_list_input: str) -> list[str]:
    """Parse the sitemap locations into and array from a string input.

    Args:
        string_or_list_input (str): Input from CLI parameter, e.g. `"https://example.com/sitemap.xml"` or `"[\'https://example.com/sitemap1.xml\', \'https://example.com/sitemap2.xml\']"`.

    Returns:
        list[str]: List of sitemap locations or URLs.
    """

    def is_list(input: str) -> bool:
        """Check if the input is a list by checking for square brackets, commas, or spaces."""

        return any([input.startswith("["), input.endswith("]"), "," in input, " " in input.strip()])

    def parse_list_input(input: str) -> list[str]:
        def normalise_list_string_to_comma_separated_items(input: str) -> str:
            """Remove square brackets and commas from the input string and return a list of comma separated items."""

            return input.strip().replace("[", "").replace("]", "").replace("  ", " ").replace(" ", ",")

        normalised_list_string = normalise_list_string_to_comma_separated_items(input)
        return [normalise_string(item) for item in normalised_list_string.split(",") if normalise_string(item)]

    if not string_or_list_input:
        return []
    if is_list(string_or_list_input):
        return parse_list_input(string_or_list_input)
    return [normalise_string(string_or_list_input)]


def parse_sitemap_filter_input(sitemap_filter: str) -> str | None:
    """Parse the input of the `sitemap_filter` argument and check whether a regular expression needs to be created from it.

    Args:
        sitemap_filter (str): Input from CLI parameter, e.g. contains `"section1"` or a regular expression `"r'(section1|section2)'"`.

    Returns:
        str | None: The filter or None if the input is empty.
    """

    def is_regex(input: str) -> bool:
        return input.startswith("r\"") or input.startswith("r\'")

    def recreate_regex_from_input(input: str) -> str:
        input_cleaned = normalise_string(input.replace("r\"", "").replace("r\'", ""))
        return rf"{input_cleaned}"

    if not sitemap_filter:
        return None
    if is_regex(sitemap_filter):
        return recreate_regex_from_input(sitemap_filter)
    return normalise_string(sitemap_filter)


def parse_sitemap_days_ago_input(sitemap_days_ago: int | str) -> DaysAgo | None:
    """Parse the input of the `sitemap_days_ago` argument and return a DaysAgo class or None if the input is empty.

    Args:
        sitemap_days_ago (int | str): Input from CLI parameter, e.g. 1, 2, or more days ago.

    Returns:
        DaysAgo | None: The sitemap DaysAgo class or None if the input is empty.
    """

    if not sitemap_days_ago and not str(sitemap_days_ago) == "0":
        return None
    if isinstance(sitemap_days_ago, str) and not sitemap_days_ago.isdigit():
        return None
    if not isinstance(sitemap_days_ago, int):
        days_ago = int(sitemap_days_ago, base=10)
        return DaysAgo(days_ago)
    return DaysAgo(sitemap_days_ago)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Submit a sitemap to IndexNow. How to run the script:

            python submit.py --host example.com --api-key a1b2c3d4 --api-key-location https://example.com/a1b2c3d4.txt --endpoint yandex --urls https://example.com --sitemap-locations https://example.com/sitemap.xml --sitemap-filter section1 --sitemap-days-ago 1

        The parameters are:

            "--host example.com": The host name of the website. Mandatory.
            "--api-key a1b2c3d4": The API key for IndexNow. Mandatory.
            "--api-key-location https://example.com/a1b2c3d4.txt": The location of the API key. Mandatory.
            "--endpoint yandex": The search engine endpoint (e.g. "indexnow", "bing", "naver", "seznam", "yandex", "yep"). Mandatory.
            "--urls https://example.com": The URL(s) to be submitted. Optional.
            "--sitemap-locations https://example.com/sitemap.xml": The location of the sitemap(s) to be submitted. Optional.
            "--sitemap-filter section1": Only submit sitemap URLs that contain "section1" or match a regular expression "r'(section1)|(section2)'". Optional.
            "--sitemap-days-ago 1": Only submit sitemap URLs that have been modified recently based on the <lastmod> tag, e.g. 1, 2, or more days ago. Optional.
        """)
    parser.add_argument("--host", type=str, help="The host name of the website, e.g. \"example.com\". Mandatory.")
    parser.add_argument("--api-key", type=str, help="The API key for IndexNow, e.g. \"a1b2c3d4\". Mandatory.")
    parser.add_argument("--api-key-location", type=str, help="The location of the API key, e.g. \"https://example.com/a1b2c3d4.txt\". Mandatory.")
    parser.add_argument("--endpoint", type=str, help="The search engine endpoint (e.g. \"indexnow\", \"bing\", \"naver\", \"seznam\", \"yandex\", \"yep\"). Mandatory.")
    parser.add_argument("--urls", nargs="?", type=str, default=None, help="The URLs to be submitted, e.g. a single URL \"https://example.com\" or multiple URLs as list \"https://example.com/page1 https://example.com/page2\". Optional.")
    parser.add_argument("--sitemap-locations", nargs="?", type=str, default=None, help="The locations of the sitemaps to be submitted, e.g. a single sitemap \"https://example.com/sitemap.xml\" or multiple sitemaps as list \"https://example.com/sitemap1.xml https://example.com/sitemap2.xml\". Optional.")
    parser.add_argument("--sitemap-filter", nargs="?", type=str, default=None, help="Only submit sitemap URLs that contain the filter string, e.g. \"section1\". Optional.")
    parser.add_argument("--sitemap-days-ago", nargs="?", type=str, default=None, help="Only submit sitemap URLs that have been modified recently based on the <lastmod> tag, e.g. 1, 2, or more days ago. Optional.")
    input = parser.parse_args()

    if not all([input.host, input.api_key, input.api_key_location, input.endpoint]):
        print(f"{Color.YELLOW}Some or all mandatory arguments for host, API key, API key location, and endpoint are missing. Aborting...{Color.OFF}")
        exit_with_failure()

    authentication = IndexNowAuthentication(
        host=input.host,
        api_key=input.api_key,
        api_key_location=input.api_key_location
    )
    endpoint = get_endpoint_from_input(input.endpoint)

    urls = parse_string_or_list_input(input.urls)
    sitemap_locations = parse_string_or_list_input(input.sitemap_locations)

    if not any([urls, sitemap_locations]):
        print(f"{Color.YELLOW}No sitemaps or URLs to submit. Aborting...{Color.OFF}")
        exit_with_failure()

    if urls:
        status_code = submit_urls_to_index_now(authentication, urls, endpoint=endpoint)
        if not is_successful_response(status_code):
            print(f"Failed to submit URLs. Status code from {endpoint.name.title()}: {Color.RED}{status_code}{Color.OFF}")
            exit_with_failure()
    else:
        print(f"{Color.YELLOW}No URLs to submit. Skipping...{Color.OFF}")

    if sitemap_locations:
        contains = parse_sitemap_filter_input(input.sitemap_filter)
        days_ago = parse_sitemap_days_ago_input(input.sitemap_days_ago)
        filter = SitemapFilter(contains=contains, date_range=days_ago)
        status_code = submit_sitemaps_to_index_now(authentication, sitemap_locations, filter=filter, endpoint=endpoint)
        if not is_successful_response(status_code):
            print(f"Failed to submit sitemaps. Status code from {endpoint.name.title()}: {Color.RED}{status_code}{Color.OFF}")
            exit_with_failure()
    else:
        print(f"{Color.YELLOW}No sitemaps to submit. Skipping...{Color.OFF}")

    exit_with_success()
