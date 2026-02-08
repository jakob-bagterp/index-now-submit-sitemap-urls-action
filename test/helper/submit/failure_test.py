import subprocess

import pytest
from colorist import Color
from constant import (FAILURE_EXIT_CODE, INVALID_API_KEY, INVALID_API_KEY_LOCATION, VALID_API_KEY,
                      VALID_API_KEY_LOCATION, VALID_HOST)
from index_now import (IndexNowAuthentication, SearchEngineEndpoint, submit_sitemaps_to_index_now,
                       submit_urls_to_index_now)
from index_now.status_code import SUCCESS_STATUS_CODES_COLLECTION

AUTHENTICATION_WITH_INVALID_API_KEY = IndexNowAuthentication(
    host=VALID_HOST,
    api_key=INVALID_API_KEY,
    api_key_location=INVALID_API_KEY_LOCATION
)

URLS = ["https://jakob-bagterp.github.io"]
SITEMAP_LOCATIONS = ["https://jakob-bagterp.github.io/sitemap.xml"]


def is_error_response(status_code: int) -> bool:
    return 400 <= status_code <= 599 if isinstance(status_code, int) else False


def test_submit_urls_from_terminal_failure() -> None:
    # Ensure that we also receive an error message when using the same submit method and parameters:
    status_code = submit_urls_to_index_now(AUTHENTICATION_WITH_INVALID_API_KEY, URLS, endpoint=SearchEngineEndpoint.BING)
    assert status_code not in SUCCESS_STATUS_CODES_COLLECTION
    assert is_error_response(status_code)

    result = subprocess.run(["python3", "./src/helper/submit.py",
                             "--host", VALID_HOST,
                             "--api-key", INVALID_API_KEY,
                             "--api-key-location", INVALID_API_KEY_LOCATION,
                             "--endpoint", "bing",
                             "--urls", URLS[0],
                             "--sitemap-locations", "",
                             ], capture_output=True, text=True)
    assert result.returncode == FAILURE_EXIT_CODE
    assert f"Failed to submit URLs. Status code from Bing: {Color.RED}" in result.stdout


def test_submit_sitemaps_from_terminal_failure() -> None:
    # Ensure that we also receive an error message when using the same submit method and parameters:
    status_code = submit_sitemaps_to_index_now(AUTHENTICATION_WITH_INVALID_API_KEY, SITEMAP_LOCATIONS, endpoint=SearchEngineEndpoint.BING)
    assert status_code not in SUCCESS_STATUS_CODES_COLLECTION
    assert is_error_response(status_code)

    result = subprocess.run(["python3", "./src/helper/submit.py",
                             "--host", VALID_HOST,
                             "--api-key", INVALID_API_KEY,
                             "--api-key-location", INVALID_API_KEY_LOCATION,
                             "--endpoint", "bing",
                             "--urls", "",
                             "--sitemap-locations", SITEMAP_LOCATIONS[0],
                             "--sitemap-filter", "",
                             "--sitemap-days-ago", "",
                             ], capture_output=True, text=True)
    assert result.returncode == FAILURE_EXIT_CODE
    assert f"Failed to submit sitemaps. Status code from Bing: {Color.RED}" in result.stdout


@pytest.mark.parametrize("host, api_key, api_key_location, endpoint", [
    ("", VALID_API_KEY, VALID_API_KEY_LOCATION, "bing"),
    (VALID_HOST, "", VALID_API_KEY_LOCATION, "bing"),
    (VALID_HOST, INVALID_API_KEY, "", "bing"),
    (VALID_HOST, INVALID_API_KEY, VALID_API_KEY_LOCATION, ""),
    ("", "", "", ""),
])
def test_submit_missing_mandatory_arguments_from_terminal_failure(host: str, api_key: str, api_key_location: str, endpoint: str) -> None:
    result = subprocess.run(["python3", "./src/helper/submit.py",
                             "--host", host,
                             "--api-key", api_key,
                             "--api-key-location", api_key_location,
                             "--endpoint", endpoint,
                             "--urls", URLS[0],
                             "--sitemap-locations", ""
                             "--sitemap-filter", "",
                             "--sitemap-days-ago", "",
                             ], capture_output=True, text=True)
    assert result.returncode == FAILURE_EXIT_CODE
    assert f"{Color.YELLOW}Some or all mandatory arguments for host, API key, API key location, and endpoint are missing. Aborting...{Color.OFF}" in result.stdout
