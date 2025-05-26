import pytest

from helper.submit import parse_string_or_list_input

EXPECTED_URL = ["https://example.com"]
EXPECTED_URLS = ["https://example.com/page1", "https://example.com/page2"]


@pytest.mark.parametrize("sitemap_locations, expected", [
    ("", []),
    (None, []),
    ("https://example.com", EXPECTED_URL),
    ("\"https://example.com\"", EXPECTED_URL),
    ('https://example.com', EXPECTED_URL),
    ('\'https://example.com\'', EXPECTED_URL),
    ("['https://example.com/page1', 'https://example.com/page2']", EXPECTED_URLS),
    ('["https://example.com/page1", "https://example.com/page2"]', EXPECTED_URLS),
    ("[\"https://example.com/page1\", \"https://example.com/page2\"]", EXPECTED_URLS),
    ('[\'https://example.com/page1\', \'https://example.com/page2\']', EXPECTED_URLS),
    ("[ 'https://example.com/page1', ' https://example.com/page2 ' ]", EXPECTED_URLS),
    ('[ "https://example.com/page1", " https://example.com/page2 "]', EXPECTED_URLS),
    ("https://example.com/page1, https://example.com/page2", EXPECTED_URLS),
    ("https://example.com, ", EXPECTED_URL),
    ("https://example.com/page1, https://example.com/page2, ", EXPECTED_URLS),
])
def test_parse_urls_input(sitemap_locations: str, expected: list[str]) -> None:
    assert parse_string_or_list_input(sitemap_locations) == expected
