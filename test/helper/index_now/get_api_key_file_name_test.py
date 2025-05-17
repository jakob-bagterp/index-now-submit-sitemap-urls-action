import pytest

from helper.index_now.api_key import get_api_key_file_name


@pytest.mark.parametrize("api_key, expected_file_name", [
    ("a1b2c3d4", "a1b2c3d4.txt"),
    ("1234567890", "1234567890.txt"),
    ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz.txt"),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ.txt"),
])
def test_get_api_key_file_name(api_key: str, expected_file_name: str) -> None:
    assert get_api_key_file_name(api_key) == expected_file_name
