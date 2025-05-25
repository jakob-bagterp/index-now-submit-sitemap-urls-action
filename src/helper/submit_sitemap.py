import argparse

from index_now import (IndexNowAuthentication, SearchEngineEndpoint,
                       submit_sitemap_to_index_now)


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


def parse_sitemap_locations(sitemap_locations: str) -> list[str]:
    """Parse the sitemap locations into and array from a string input.

    Args:
        sitemap_locations (str): Input from CLI parameter, e.g. `"https://example.com/sitemap.xml"` or `"[\'https://example.com/sitemap1.xml\', \'https://example.com/sitemap2.xml\']"`.

    Returns:
        list[str]: List of sitemap locations.
    """

    if not sitemap_locations:
        return []
    if any([sitemap_locations.startswith("["), sitemap_locations.endswith("]"), "," in sitemap_locations]):  # If the input contains a list of sitemap locations.
        sitemap_locations = sitemap_locations.replace("[", "").replace("]", "")
        return [sitemap_location.replace('"', "").replace("'", "").strip() for sitemap_location in sitemap_locations.split(",")]
    return [sitemap_locations.strip()]  # If the input is a single sitemap location.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Submit a sitemap to IndexNow. How to run the script:

            python submit_sitemap.py example.com a1b2c3d4 https://example.com/a1b2c3d4.txt https://example.com/sitemap.xml yandex

        The parameters are:

            "example.com": The host name of the website.
            "a1b2c3d4": The API key for IndexNow.
            "https://example.com/a1b2c3d4.txt": The location of the API key.
            "https://example.com/sitemap.xml": The location of the sitemap to be submitted.
            "yandex": The search engine endpoint (e.g. "indexnow", "bing", "naver", "seznam", "yandex", "yep").
        """)
    parser.add_argument("host", type=str, help="The host name of the website, e.g. \"example.com\".")
    parser.add_argument("api_key", type=str, help="The API key for IndexNow, e.g. \"a1b2c3d4\".")
    parser.add_argument("api_key_location", type=str, help="The location of the API key, e.g. \"https://example.com/a1b2c3d4.txt\".")
    parser.add_argument("sitemap_location", type=str, help="The location of the sitemap to be submitted, e.g. \"https://example.com/sitemap.xml\".")
    parser.add_argument("endpoint", type=str, help="The search engine endpoint (e.g. \"indexnow\", \"bing\", \"naver\", \"seznam\", \"yandex\", \"yep\").")
    input = parser.parse_args()
    authentication = IndexNowAuthentication(
        host=input.host,
        api_key=input.api_key,
        api_key_location=input.api_key_location
    )
    endpoint = get_endpoint_from_input(input.endpoint)
    submit_sitemap_to_index_now(authentication, input.sitemap_location, endpoint=endpoint)
