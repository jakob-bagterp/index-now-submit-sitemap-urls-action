import pytest
from index_now.sitemap import filter_urls

from helper.submit import parse_sitemap_filter_input


@pytest.mark.parametrize("sitemap_filter_input, expected", [
    ("", None),
    ('', None),
    ("section1", "section1"),
    ('section1', "section1"),
    ("\'section1\'", "section1"),
    ('\"section1\"', "section1"),
    ("r'(section1|section2)'", r"(section1|section2)"),
    ('r"(section1|section2)"', r"(section1|section2)"),
]
)
def test_parse_sitemap_filter_input(sitemap_filter_input: str, expected: str | None) -> None:
    result = parse_sitemap_filter_input(sitemap_filter_input)
    assert result == expected


URLS = [
    "https://example.com/section1/page1",
    "https://example.com/section2/page1",
    "https://example.com/section2/page2",
]


@pytest.mark.parametrize("sitemap_urls, sitemap_filter_input, expected", [
    (URLS, "", URLS),
    (URLS, '', URLS),
    (URLS, "section1", ["https://example.com/section1/page1"]),
    (URLS, 'section1', ["https://example.com/section1/page1"]),
    (URLS, "\'section1\'", ["https://example.com/section1/page1"]),
    (URLS, '\"section1\"', ["https://example.com/section1/page1"]),
    (URLS, "section2", ["https://example.com/section2/page1", "https://example.com/section2/page2"]),
    (URLS, "section3", []),
    (URLS, r"(section1|section2)", URLS),
    (URLS, r"(section1|section3)", ["https://example.com/section1/page1"]),
    (URLS, "r'(section1|section2)'", URLS),
    (URLS, 'r"(section1|section2)"', URLS),
]
)
def test_filter_urls(sitemap_urls: list[str], sitemap_filter_input: str, expected: list[str]) -> None:
    contains = parse_sitemap_filter_input(sitemap_filter_input)
    result = filter_urls(sitemap_urls, contains)
    assert result == expected
