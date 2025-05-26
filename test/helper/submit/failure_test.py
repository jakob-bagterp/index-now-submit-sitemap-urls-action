import subprocess

import pytest


def test_submit_sitemap_failure_from_terminal() -> None:
    with pytest.raises(SystemExit) as pytest_wrapped_exit:
        subprocess.call(["python3", "./src/helper/submit_sitemap.py",
                        "jakob-bagterp.github.io",
                         "invalid",
                         "https://jakob-bagterp.github.io/invalid.txt",
                         "bing",
                         "--sitemap-locations", "https://jakob-bagterp.github.io/sitemap.xml",
                         "--urls", "",
                         ])
    assert pytest_wrapped_exit.type == SystemExit
    assert pytest_wrapped_exit.value.code == 1


def test_submit_urls_failure_from_terminal() -> None:
    with pytest.raises(SystemExit) as pytest_wrapped_exit:
        subprocess.call(["python3", "./src/helper/submit_sitemap.py",
                        "jakob-bagterp.github.io",
                         "invalid",
                         "https://jakob-bagterp.github.io/invalid.txt",
                         "bing",
                         "--sitemap-locations", "",
                         "--urls", "https://jakob-bagterp.github.io",
                         ])
    assert pytest_wrapped_exit.type == SystemExit
    assert pytest_wrapped_exit.value.code == 1
