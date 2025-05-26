import subprocess

import pytest
from colorist import Color
from constant import (SUCCESS_EXIT_CODE, VALID_API_KEY, VALID_API_KEY_LOCATION,
                      VALID_HOST)


@pytest.mark.parametrize("urls", [
    "https://jakob-bagterp.github.io/",
    "https://jakob-bagterp.github.io/, https://jakob-bagterp.github.io/index-now-submit-sitemap-urls-action/"
])
def test_submit_urls_from_terminal(urls: str, capfd: object) -> None:
    status_code = subprocess.call(["python3", "./src/helper/submit.py",
                                   VALID_HOST,
                                   VALID_API_KEY,
                                   VALID_API_KEY_LOCATION,
                                   "yandex",
                                   "--sitemap-locations", "",
                                   "--urls", urls,
                                   ])
    assert status_code == SUCCESS_EXIT_CODE
    terminal_output, _ = capfd.readouterr()
    assert f"URL(s) submitted successfully to the IndexNow API:{Color.OFF}" in terminal_output
    assert f"Status code: {Color.GREEN}200{Color.OFF}" or f"Status code: {Color.GREEN}202{Color.OFF}" in terminal_output
