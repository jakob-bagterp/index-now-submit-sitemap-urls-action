import argparse

from index_now import (IndexNowAuthentication, SearchEngineEndpoint,
                       submit_sitemaps_to_index_now, submit_urls_to_index_now)

from .result import (exit_with_failure, exit_with_success,
                     is_successful_response)


def get_endpoint_from_input(endpoint: str) -> SearchEngineEndpoint:
    """Get a search engine endpoint from text input.

    Args:
        endpoint (str): Input from CLI parameter, e.g `"indexnow"`, `"bing"`, `"naver"`, `"seznam"`, `"yandex"`, `"yep"`.

    Returns:
        SearchEngineEndpoint: Search engine endpoint. Fallback is Microsoft Bing.
    """

    match endpoint:
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


def parse_string_or_list_input(string_or_list_input: str) -> list[str]:
    """Parse the sitemap locations into and array from a string input.

    Args:
        string_or_list_input (str): Input from CLI parameter, e.g. `"https://example.com/sitemap.xml"` or `"[\'https://example.com/sitemap1.xml\', \'https://example.com/sitemap2.xml\']"`.

    Returns:
        list[str]: List of sitemap locations or URLs.
    """

    def is_list(input: str) -> bool:
        """Check if the input is a list by checking for square brackets and commas."""

        return any([input.startswith("["), input.endswith("]"), "," in input])

    def remove_list_brackets(input: str) -> str:
        """Remove square brackets from the input string."""

        return input.replace("[", "").replace("]", "")

    def normalize(input: str) -> str:
        """Normalize the input string by removing quotes and whitespace."""

        return input.replace('"', "").replace("'", "").strip()

    if not string_or_list_input:
        return []
    if is_list(string_or_list_input):
        string_or_list_input = remove_list_brackets(string_or_list_input)
        return [normalize(item) for item in string_or_list_input.split(",") if item.strip()]
    return [normalize(string_or_list_input)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Submit a sitemap to IndexNow. How to run the script:

            python submit_sitemap.py example.com a1b2c3d4 https://example.com/a1b2c3d4.txt yandex --sitemap-locations https://example.com/sitemap.xml --urls https://example.com

        The parameters are:

            "example.com": The host name of the website.
            "a1b2c3d4": The API key for IndexNow.
            "https://example.com/a1b2c3d4.txt": The location of the API key.
            "yandex": The search engine endpoint (e.g. "indexnow", "bing", "naver", "seznam", "yandex", "yep").
            "https://example.com/sitemap.xml": The location of the sitemap(s) to be submitted. Optional.
            "https://example.com": The URL(s) to be submitted. Optional.
        """)
    parser.add_argument("host", type=str, help="The host name of the website, e.g. \"example.com\".")
    parser.add_argument("api_key", type=str, help="The API key for IndexNow, e.g. \"a1b2c3d4\".")
    parser.add_argument("api_key_location", type=str, help="The location of the API key, e.g. \"https://example.com/a1b2c3d4.txt\".")
    parser.add_argument("endpoint", type=str, help="The search engine endpoint (e.g. \"indexnow\", \"bing\", \"naver\", \"seznam\", \"yandex\", \"yep\").")
    parser.add_argument("--sitemap-locations", nargs="?", type=str, default=None, help="The locations of the sitemaps to be submitted, e.g. a single sitemap \"https://example.com/sitemap.xml\" or multiple sitemaps as comma separated list \"https://example.com/sitemap1.xml, https://example.com/sitemap2.xml\".")
    parser.add_argument("--urls", nargs="?", type=str, default=None, help="The URLs to be submitted, e.g. a single URL \"https://example.com\" or multiple URLs as comma separated list \"https://example.com/page1, https://example.com/page2\".")
    input = parser.parse_args()

    authentication = IndexNowAuthentication(
        host=input.host,
        api_key=input.api_key,
        api_key_location=input.api_key_location
    )
    endpoint = get_endpoint_from_input(input.endpoint)

    sitemap_locations = parse_string_or_list_input(input.sitemap_locations)
    if sitemap_locations:
        status_code = submit_sitemaps_to_index_now(authentication, sitemap_locations, endpoint=endpoint)
        if not is_successful_response(status_code):
            print(f"Failed to submit sitemaps with status code: {status_code}")
            exit_with_failure()
    else:
        print("No sitemaps to submit. Skipping...")

    urls = parse_string_or_list_input(input.urls)
    if urls:
        status_code = submit_urls_to_index_now(authentication, urls, endpoint=endpoint)
        if not is_successful_response(status_code):
            print(f"Failed to submit URLs with status code: {status_code}")
            exit_with_failure()
    else:
        print("No URLs to submit. Skipping...")

    exit_with_success()
