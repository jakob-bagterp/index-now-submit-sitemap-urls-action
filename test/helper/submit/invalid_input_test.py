import subprocess

from colorist import Color
from constant import FAILURE_EXIT_CODE, VALID_API_KEY, VALID_API_KEY_LOCATION, VALID_HOST


def test_submit_with_unknown_endpoint_from_terminal() -> None:
    result = subprocess.run(
        [
            "python3",
            "./src/helper/submit.py",
            "--host",
            VALID_HOST,
            "--api-key",
            VALID_API_KEY,
            "--api-key-location",
            VALID_API_KEY_LOCATION,
            "--endpoint",
            "seznm",
            "--urls",
            "https://jakob-bagterp.github.io/index-now-submit-sitemap-urls-action/",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == FAILURE_EXIT_CODE
    assert (
        f"{Color.YELLOW}Unknown endpoint: seznm. Options: indexnow, bing, naver, seznam, yandex, yep. Aborting...{Color.OFF}"
        in result.stdout
    )
    assert "submitted successfully" not in result.stdout


def test_submit_with_invalid_retries_from_terminal() -> None:
    result = subprocess.run(
        [
            "python3",
            "./src/helper/submit.py",
            "--host",
            VALID_HOST,
            "--api-key",
            VALID_API_KEY,
            "--api-key-location",
            VALID_API_KEY_LOCATION,
            "--endpoint",
            "seznam",
            "--urls",
            "https://jakob-bagterp.github.io/index-now-submit-sitemap-urls-action/",
            "--retries",
            "-1",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == FAILURE_EXIT_CODE
    assert (
        f"{Color.YELLOW}Invalid number of retries: -1. Use a whole number of 0 or more. Aborting...{Color.OFF}"
        in result.stdout
    )
    assert "submitted successfully" not in result.stdout
