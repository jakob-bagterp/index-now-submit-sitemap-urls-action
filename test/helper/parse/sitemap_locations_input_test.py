import pytest

from helper.submit import parse_string_or_list_input

EXPECTED_SITEMAP_LOCATION = ["https://example.com/sitemap.xml"]
EXPECTED_SITEMAP_LOCATIONS = ["https://example.com/sitemap1.xml", "https://example.com/sitemap2.xml"]


@pytest.mark.parametrize("sitemap_locations, expected", [
    ("", []),
    (None, []),
    ("https://example.com/sitemap.xml", EXPECTED_SITEMAP_LOCATION),
    ("\"https://example.com/sitemap.xml\"", EXPECTED_SITEMAP_LOCATION),
    ('https://example.com/sitemap.xml', EXPECTED_SITEMAP_LOCATION),
    ('\'https://example.com/sitemap.xml\'', EXPECTED_SITEMAP_LOCATION),
    ("['https://example.com/sitemap1.xml', 'https://example.com/sitemap2.xml']", EXPECTED_SITEMAP_LOCATIONS),
    ('["https://example.com/sitemap1.xml", "https://example.com/sitemap2.xml"]', EXPECTED_SITEMAP_LOCATIONS),
    ("\"['https://example.com/sitemap1.xml', 'https://example.com/sitemap2.xml']\"", EXPECTED_SITEMAP_LOCATIONS),
    ('\'["https://example.com/sitemap1.xml", "https://example.com/sitemap2.xml"]\'', EXPECTED_SITEMAP_LOCATIONS),
    ("[\"https://example.com/sitemap1.xml\", \"https://example.com/sitemap2.xml\"]", EXPECTED_SITEMAP_LOCATIONS),
    ('[\'https://example.com/sitemap1.xml\', \'https://example.com/sitemap2.xml\']', EXPECTED_SITEMAP_LOCATIONS),
    ("[ 'https://example.com/sitemap1.xml', ' https://example.com/sitemap2.xml ' ]", EXPECTED_SITEMAP_LOCATIONS),
    ('[ "https://example.com/sitemap1.xml", " https://example.com/sitemap2.xml "]', EXPECTED_SITEMAP_LOCATIONS),
    ("https://example.com/sitemap1.xml, https://example.com/sitemap2.xml", EXPECTED_SITEMAP_LOCATIONS),
    ("https://example.com/sitemap1.xml,https://example.com/sitemap2.xml", EXPECTED_SITEMAP_LOCATIONS),
    ("https://example.com/sitemap1.xml https://example.com/sitemap2.xml", EXPECTED_SITEMAP_LOCATIONS),
    ("  https://example.com/sitemap1.xml https://example.com/sitemap2.xml  ", EXPECTED_SITEMAP_LOCATIONS),
    ("https://example.com/sitemap.xml, ", EXPECTED_SITEMAP_LOCATION),
    ("https://example.com/sitemap1.xml, https://example.com/sitemap2.xml, ", EXPECTED_SITEMAP_LOCATIONS),
])
def test_parse_sitemap_locations_input(sitemap_locations: str, expected: list[str]) -> None:
    assert parse_string_or_list_input(sitemap_locations) == expected
