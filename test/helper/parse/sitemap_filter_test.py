import pytest
from index_now.sitemap.filter.sitemap import SitemapFilter, filter_sitemap_urls
from index_now.sitemap.parse import SitemapUrl

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

SITEMAP_URLS = [SitemapUrl(url) for url in URLS]


@pytest.mark.parametrize("sitemap_urls, sitemap_filter_input, expected", [
    (SITEMAP_URLS, "", URLS),
    (SITEMAP_URLS, '', URLS),
    (SITEMAP_URLS, "section1", ["https://example.com/section1/page1"]),
    (SITEMAP_URLS, 'section1', ["https://example.com/section1/page1"]),
    (SITEMAP_URLS, "\'section1\'", ["https://example.com/section1/page1"]),
    (SITEMAP_URLS, '\"section1\"', ["https://example.com/section1/page1"]),
    (SITEMAP_URLS, "section2", ["https://example.com/section2/page1", "https://example.com/section2/page2"]),
    (SITEMAP_URLS, "section3", []),
    (SITEMAP_URLS, r"(section1|section2)", URLS),
    (SITEMAP_URLS, r"(section1|section3)", ["https://example.com/section1/page1"]),
    (SITEMAP_URLS, "r'(section1|section2)'", URLS),
    (SITEMAP_URLS, 'r"(section1|section2)"', URLS),
]
)
def test_filter_urls(sitemap_urls: list[SitemapUrl], sitemap_filter_input: str, expected: list[str]) -> None:
    contains = parse_sitemap_filter_input(sitemap_filter_input)
    filter = SitemapFilter(contains=contains)
    result = filter_sitemap_urls(sitemap_urls, filter)
    assert result == expected
