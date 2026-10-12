import pytest

from helper.submit import DEFAULT_RETRIES, parse_retries_input


@pytest.mark.parametrize(
    "input, expected_retries",
    [("3", 3), ("0", 0), ("5", 5), (" 2 ", 2), ('"4"', 4), ("", DEFAULT_RETRIES), (None, DEFAULT_RETRIES)],
)
def test_parse_retries_input(input: str | None, expected_retries: int) -> None:
    assert parse_retries_input(input) == expected_retries


@pytest.mark.parametrize("input", ["-1", "three", "1.5", "3 retries"])
def test_parse_retries_input_raises_error_for_invalid_input(input: str) -> None:
    with pytest.raises(ValueError, match="Invalid number of retries"):
        parse_retries_input(input)


def test_default_retries() -> None:
    assert DEFAULT_RETRIES == 3
