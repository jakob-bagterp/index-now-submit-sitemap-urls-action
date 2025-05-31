import subprocess

import pytest
from colorist import Color
from constant import (SUCCESS_EXIT_CODE, VALID_API_KEY, VALID_API_KEY_LOCATION,
                      VALID_HOST)


@pytest.mark.parametrize("sitemap_locations", [
    "https://jakob-bagterp.github.io/sitemap.xml",
    "https://jakob-bagterp.github.io/sitemap.xml, https://jakob-bagterp.github.io/index-now-submit-sitemap-urls-action/sitemap.xml"
])
def test_submit_sitemaps_from_terminal(sitemap_locations: str) -> None:
    result = subprocess.run(["python3", "./src/helper/submit.py",
                             VALID_HOST,
                             VALID_API_KEY,
                             VALID_API_KEY_LOCATION,
                             "yandex",
                             "--urls", "",
                             "--sitemap-locations", sitemap_locations,
                             "--sitemap-filter", "",
                             "--sitemap-days-ago", "",
                             ], capture_output=True, text=True)
    assert result.returncode == SUCCESS_EXIT_CODE
    assert f"URL(s) submitted successfully to the IndexNow API:{Color.OFF}" in result.stdout
    assert f"Status code: {Color.GREEN}200{Color.OFF}" or f"Status code: {Color.GREEN}202{Color.OFF}" in result.stdout
