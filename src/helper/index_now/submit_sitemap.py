import sys
from dataclasses import dataclass

from index_now import (IndexNowAuthentication, SearchEngineEndpoint,
                       submit_sitemap_to_index_now)


@dataclass(slots=True, frozen=True)
class InputForSubmitSitemap:
    host: str
    api_key: str
    api_key_location: str
    sitemap_url: str
    endpoint: str


def get_submit_sitemap_cli_input_parameters(parameters: list[str]) -> InputForSubmitSitemap:
    """Extract input parameters from command line arguments.

    Example:
        How to run the script:

        ```bash
        python submit_sitemap.py example.com a1b2c3d4 https://example.com/a1b2c3d4.txt https://example.com/sitemap.xml yandex
        ```

    Args:
        parameters (list[str]): List of command line arguments. The parameters are:

        * `example.com`: The host name of the website.
        * `a1b2c3d4`: The API key for IndexNow.
        * `https://example.com/a1b2c3d4.txt`: The location of the API key.
        * `https://example.com/sitemap.xml`: The URL of the sitemap to be submitted.
        * `yandex`: The search engine endpoint (e.g. "indexnow", "bing", "naver", "seznam", "yandex", "yep").

    Returns:
        InputForSubmitSitemap: Data class with the input parameters.
    """

    return InputForSubmitSitemap(
        host=parameters[1],
        api_key=parameters[2],
        api_key_location=parameters[3],
        sitemap_url=parameters[4],
        endpoint=parameters[5]
    )


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
    input = get_submit_sitemap_cli_input_parameters(sys.argv)
    authentication = IndexNowAuthentication(
        host=input.host,
        api_key=input.api_key,
        api_key_location=input.api_key_location
    )
    endpoint = get_endpoint_from_input(input.endpoint)
    submit_sitemap_to_index_now(authentication, input.sitemap_url, endpoint=endpoint)
