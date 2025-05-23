import pytest
from index_now import SearchEngineEndpoint

from helper.submit_sitemap import get_endpoint_from_input


@pytest.mark.parametrize("input, expected_endpoint", [
    ("indexnow", SearchEngineEndpoint.INDEXNOW),
    ("bing", SearchEngineEndpoint.BING),
    ("naver", SearchEngineEndpoint.NAVER),
    ("seznam", SearchEngineEndpoint.SEZNAM),
    ("yandex", SearchEngineEndpoint.YANDEX),
    ("yep", SearchEngineEndpoint.YEP),
    ("invalid", SearchEngineEndpoint.BING),
    (None, SearchEngineEndpoint.BING),
    (1, SearchEngineEndpoint.BING),
])
def test_get_endpoint_from_input(input: str, expected_endpoint: SearchEngineEndpoint) -> None:
    assert get_endpoint_from_input(input) is expected_endpoint
