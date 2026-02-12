import subprocess

from colorist import Color
from constant import FAILURE_EXIT_CODE, VALID_API_KEY, VALID_API_KEY_LOCATION, VALID_HOST


def test_submit_nothing_from_terminal() -> None:
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
            "yandex",
            "--urls",
            "",
            "--sitemap-locations",
            "",
            "--sitemap-filter",
            "",
            "--sitemap-days-ago",
            "",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == FAILURE_EXIT_CODE
    assert f"{Color.YELLOW}No sitemaps or URLs to submit. Aborting...{Color.OFF}" in result.stdout
