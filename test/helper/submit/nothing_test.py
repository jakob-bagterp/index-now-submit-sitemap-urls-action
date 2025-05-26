import subprocess


def test_submit_nothing_from_terminal(capfd: object) -> None:
    subprocess.call(["python3", "./src/helper/submit.py",
                     "jakob-bagterp.github.io",
                     "6d71a14ac15c4c41a0c19e641f659208",
                     "https://jakob-bagterp.github.io/index-now-api-key.txt",
                     "yandex",
                     "--sitemap-locations", "",
                     "--urls", "",
                     ])
    terminal_output, _ = capfd.readouterr()
    assert "No sitemaps to submit. Skipping..." in terminal_output
    assert "No URLs to submit. Skipping..." in terminal_output
