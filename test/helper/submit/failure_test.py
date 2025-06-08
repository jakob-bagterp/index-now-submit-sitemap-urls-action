import subprocess

from constant import (FAILURE_EXIT_CODE, INVALID_API_KEY,
                      INVALID_API_KEY_LOCATION, VALID_HOST)
from index_now import (IndexNowAuthentication, SearchEngineEndpoint,
                       submit_sitemaps_to_index_now, submit_urls_to_index_now)

from helper.submit import SUCCESS_STATUS_CODES

AUTHENTICATION_WITH_INVALID_API_KEY = IndexNowAuthentication(
    host=VALID_HOST,
    api_key=INVALID_API_KEY,
    api_key_location=INVALID_API_KEY_LOCATION
)

URLS = ["https://jakob-bagterp.github.io"]
SITEMAP_LOCATIONS = ["https://jakob-bagterp.github.io/sitemap.xml"]


def is_error_response(status_code: int) -> bool:
    status_code_string = str(status_code)
    return status_code_string.startswith("4") or status_code_string.startswith("5")


def test_submit_urls_from_terminal_failure() -> None:
    # Ensure that we also receive an error message when using the same submit method and parameters:
    status_code = submit_urls_to_index_now(AUTHENTICATION_WITH_INVALID_API_KEY, URLS, endpoint=SearchEngineEndpoint.BING)
    assert status_code not in SUCCESS_STATUS_CODES
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
    assert "Failed to submit URLs. Status code response from Bing:" in result.stdout


def test_submit_sitemaps_from_terminal_failure() -> None:
    # Ensure that we also receive an error message when using the same submit method and parameters:
    status_code = submit_sitemaps_to_index_now(AUTHENTICATION_WITH_INVALID_API_KEY, SITEMAP_LOCATIONS, endpoint=SearchEngineEndpoint.BING)
    assert status_code not in SUCCESS_STATUS_CODES
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
    assert "Failed to submit sitemaps. Status code response from Bing:" in result.stdout
