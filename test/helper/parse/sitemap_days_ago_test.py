import pytest
from _mock_data.sitemap import SITEMAP_URLS, URLS
from index_now import DaysAgo
from index_now.sitemap.filter.sitemap import SitemapFilter, filter_sitemap_urls
from index_now.sitemap.parse import SitemapUrl

from helper.submit import parse_sitemap_days_ago_input


@pytest.mark.parametrize("sitemap_days_ago_input, expected", [
    ("", None),
    ('', None),
    (1, DaysAgo(1)),
    ("1", DaysAgo(1)),
    (2, DaysAgo(2)),
    ("2", DaysAgo(2)),
    (3, DaysAgo(3)),
    ("3", DaysAgo(3)),
    ("not valid", None),
])
def test_parse_sitemap_days_ago_input(sitemap_days_ago_input: int | str, expected: DaysAgo | None) -> None:
    result = parse_sitemap_days_ago_input(sitemap_days_ago_input)
    assert result == expected


@pytest.mark.parametrize("sitemap_urls, sitemap_days_ago_input, expected", [
    (SITEMAP_URLS, "", URLS),
    (SITEMAP_URLS, '', URLS),
    (SITEMAP_URLS, 0, URLS[:1]),
    (SITEMAP_URLS, "0", URLS[:1]),
    (SITEMAP_URLS, 1, URLS[:2]),
    (SITEMAP_URLS, "1", URLS[:2]),
    (SITEMAP_URLS, 2, URLS),
    (SITEMAP_URLS, "2", URLS),
    (SITEMAP_URLS, 3, URLS),
    (SITEMAP_URLS, "3", URLS),
    (SITEMAP_URLS, "not valid", URLS),
])
def test_days_ago_urls(sitemap_urls: list[SitemapUrl], sitemap_days_ago_input: int | str, expected: list[str]) -> None:
    days_ago = parse_sitemap_days_ago_input(sitemap_days_ago_input)
    filter = SitemapFilter(date_range=days_ago)
    result = filter_sitemap_urls(sitemap_urls, filter)
    assert result == expected
