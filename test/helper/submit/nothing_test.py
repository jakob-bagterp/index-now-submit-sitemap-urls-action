import subprocess

from constant import SUCCESS_EXIT_CODE


def test_submit_nothing_from_terminal(capfd: object) -> None:
    status_code = subprocess.call(["python3", "./src/helper/submit.py",
                                   "jakob-bagterp.github.io",
                                   "6d71a14ac15c4c41a0c19e641f659208",
                                   "https://jakob-bagterp.github.io/index-now-api-key.txt",
                                   "yandex",
                                   "--sitemap-locations", "",
                                   "--urls", "",
                                   ])
    assert status_code == SUCCESS_EXIT_CODE
    terminal_output, _ = capfd.readouterr()
    assert "No sitemaps to submit. Skipping..." in terminal_output
    assert "No URLs to submit. Skipping..." in terminal_output
