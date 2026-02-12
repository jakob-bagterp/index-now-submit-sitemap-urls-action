import subprocess

import pytest
from colorist import Color
from constant import SUCCESS_EXIT_CODE, VALID_API_KEY, VALID_API_KEY_LOCATION, VALID_HOST


@pytest.mark.parametrize(
    "urls",
    [
        "https://jakob-bagterp.github.io/",
        "https://jakob-bagterp.github.io/, https://jakob-bagterp.github.io/index-now-submit-sitemap-urls-action/",
    ],
)
def test_submit_urls_from_terminal(urls: str) -> None:
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
            urls,
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
    assert result.returncode == SUCCESS_EXIT_CODE
    assert f"URL(s) were submitted successfully to this IndexNow API endpoint:{Color.OFF}" in result.stdout
    assert f"Status code: {Color.GREEN}200{Color.OFF}" or f"Status code: {Color.GREEN}202{Color.OFF}" in result.stdout
