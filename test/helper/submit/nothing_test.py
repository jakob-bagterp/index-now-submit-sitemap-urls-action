import subprocess

from constant import (SUCCESS_EXIT_CODE, VALID_API_KEY, VALID_API_KEY_LOCATION,
                      VALID_HOST)


def test_submit_nothing_from_terminal(capfd: object) -> None:
    status_code = subprocess.call(["python3", "./src/helper/submit.py",
                                   VALID_HOST,
                                   VALID_API_KEY,
                                   VALID_API_KEY_LOCATION,
                                   "yandex",
                                   "--sitemap-locations", "",
                                   "--urls", "",
                                   ])
    assert status_code == SUCCESS_EXIT_CODE
    terminal_output, _ = capfd.readouterr()
    assert "No sitemaps to submit. Skipping..." in terminal_output
    assert "No URLs to submit. Skipping..." in terminal_output
