import subprocess

from constant import EXIT_CODE_FAILURE


def test_submit_sitemaps_from_terminal_failure() -> None:
    exit_code = subprocess.call(["python3", "./src/helper/submit_sitemap.py",
                                 "jakob-bagterp.github.io",
                                 "invalid",
                                 "https://jakob-bagterp.github.io/invalid.txt",
                                 "bing",
                                 "--sitemap-locations", "https://jakob-bagterp.github.io/sitemap.xml",
                                 "--urls", "",
                                 ])
    assert exit_code == EXIT_CODE_FAILURE


def test_submit_urls_from_terminal_failure() -> None:
    exit_code = subprocess.call(["python3", "./src/helper/submit_sitemap.py",
                                 "jakob-bagterp.github.io",
                                 "invalid",
                                 "https://jakob-bagterp.github.io/invalid.txt",
                                 "bing",
                                 "--sitemap-locations", "",
                                 "--urls", "https://jakob-bagterp.github.io",
                                 ])
    assert exit_code == EXIT_CODE_FAILURE
