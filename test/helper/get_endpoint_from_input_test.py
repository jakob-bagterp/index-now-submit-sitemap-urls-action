import pytest
from index_now import SearchEngineEndpoint

from helper.submit import get_endpoint_from_input


@pytest.mark.parametrize("input, expected_endpoint", [
    ("indexnow", SearchEngineEndpoint.INDEXNOW),
    ("IndexNow", SearchEngineEndpoint.INDEXNOW),
    ("bing", SearchEngineEndpoint.BING),
    ("Bing", SearchEngineEndpoint.BING),
    ("naver", SearchEngineEndpoint.NAVER),
    ("Naver", SearchEngineEndpoint.NAVER),
    ("seznam", SearchEngineEndpoint.SEZNAM),
    ("Seznam", SearchEngineEndpoint.SEZNAM),
    ("yandex", SearchEngineEndpoint.YANDEX),
    ("Yandex", SearchEngineEndpoint.YANDEX),
    ("yep", SearchEngineEndpoint.YEP),
    ("Yep", SearchEngineEndpoint.YEP),
    ("invalid", SearchEngineEndpoint.BING),
    (None, SearchEngineEndpoint.BING),
    (1, SearchEngineEndpoint.BING),
])
def test_get_endpoint_from_input(input: str, expected_endpoint: SearchEngineEndpoint) -> None:
    assert get_endpoint_from_input(input) is expected_endpoint
