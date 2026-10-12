import pytest
from index_now import SearchEngineEndpoint

from helper.submit import get_endpoint_from_input


@pytest.mark.parametrize(
    "input, expected_endpoint",
    [
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
        (" seznam ", SearchEngineEndpoint.SEZNAM),
    ],
)
def test_get_endpoint_from_input(input: str, expected_endpoint: SearchEngineEndpoint) -> None:
    assert get_endpoint_from_input(input) is expected_endpoint


@pytest.mark.parametrize("input", ["invalid", "seznm", "https://example.com/indexnow", "", None, 1])
def test_get_endpoint_from_input_raises_error_for_unknown_endpoint(input: str) -> None:
    with pytest.raises(ValueError, match="Unknown endpoint"):
        get_endpoint_from_input(input)
