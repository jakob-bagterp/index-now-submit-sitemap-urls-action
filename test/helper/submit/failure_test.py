import subprocess

from constant import FAILURE_EXIT_CODE
from index_now import (IndexNowAuthentication, SearchEngineEndpoint,
                       submit_sitemaps_to_index_now, submit_urls_to_index_now)

from helper.result import SUCCESS_STATUS_CODES

VALID_HOST = "jakob-bagterp.github.io"
INVALID_API_KEY = "invalid"
INVALID_API_KEY_LOCATION = "https://jakob-bagterp.github.io/invalid.txt"

AUTHENTICATION = IndexNowAuthentication(
    host=VALID_HOST,
    api_key=INVALID_API_KEY,
    api_key_location=INVALID_API_KEY_LOCATION
)

SITEMAP_LOCATIONS = ["https://jakob-bagterp.github.io/sitemap.xml"]
URLS = ["https://jakob-bagterp.github.io"]


def test_submit_sitemaps_from_terminal_failure() -> None:
    # Ensure that we also receive an error message when using the same submit method and parameters:
    status_code = submit_sitemaps_to_index_now(AUTHENTICATION, SITEMAP_LOCATIONS, endpoint=SearchEngineEndpoint.BING)
    assert status_code not in SUCCESS_STATUS_CODES

    exit_code = subprocess.call(["python3", "./src/helper/submit.py",
                                 VALID_HOST,
                                 INVALID_API_KEY,
                                 INVALID_API_KEY_LOCATION,
                                 "bing",
                                 "--sitemap-locations", SITEMAP_LOCATIONS[0],
                                 "--urls", "",
                                 ])
    assert exit_code == FAILURE_EXIT_CODE


def test_submit_urls_from_terminal_failure() -> None:
    # Ensure that we also receive an error message when using the same submit method and parameters:
    status_code = submit_urls_to_index_now(AUTHENTICATION, URLS, endpoint=SearchEngineEndpoint.BING)
    assert status_code not in SUCCESS_STATUS_CODES

    exit_code = subprocess.call(["python3", "./src/helper/submit.py",
                                 VALID_HOST,
                                 INVALID_API_KEY,
                                 INVALID_API_KEY_LOCATION,
                                 "bing",
                                 "--sitemap-locations", "",
                                 "--urls", URLS[0],
                                 ])
    assert exit_code == FAILURE_EXIT_CODE
