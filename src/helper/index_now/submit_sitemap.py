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
            return SearchEngineEndpoint.MICROSOFT_BING
        case "naver":
            return SearchEngineEndpoint.NAVER
        case "seznam":
            return SearchEngineEndpoint.SEZNAM
        case "yandex":
            return SearchEngineEndpoint.YANDEX
        case "yep":
            return SearchEngineEndpoint.YEP
        case _:
            return SearchEngineEndpoint.MICROSOFT_BING


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Submit a sitemap to IndexNow. How to run the script:

            python submit_sitemap.py example.com a1b2c3d4 https://example.com/a1b2c3d4.txt https://example.com/sitemap.xml yandex

        The parameters are:

            \"example.com\": The host name of the website.
            \"a1b2c3d4\": The API key for IndexNow.
            \"https://example.com/a1b2c3d4.txt\": The location of the API key.
            \"https://example.com/sitemap.xml\": The URL of the sitemap to be submitted.
            \"yandex\": The search engine endpoint (e.g. "indexnow", "bing", "naver", "seznam", "yandex", "yep").
        """)
    parser.add_argument("host", type=str, required=True, help="The host name of the website, e.g. \"example.com\".")
    parser.add_argument("api_key", type=str, required=True, help="The API key for IndexNow, e.g. \"a1b2c3d4\".")
    parser.add_argument("api_key_location", type=str, required=True, help="The location of the API key, e.g. \"https://example.com/a1b2c3d4.txt\".")
    parser.add_argument("sitemap_url", type=str, required=True, help="The URL of the sitemap to be submitted, e.g. \"https://example.com/sitemap.xml\".")
    parser.add_argument("endpoint", type=str, required=False, help="The search engine endpoint (e.g. \"indexnow\", \"bing\", \"naver\", \"seznam\", \"yandex\", \"yep\").")
    input = parser.parse_args()
    authentication = IndexNowAuthentication(
        host=input.host,
        api_key=input.api_key,
        api_key_location=input.api_key_location
    )
    endpoint = get_endpoint_from_input(input.endpoint)
    submit_sitemap_to_index_now(authentication, input.sitemap_url, endpoint=endpoint)
