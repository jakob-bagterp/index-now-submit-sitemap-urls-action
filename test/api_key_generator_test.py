import re

from helper.index_now.generate_api_key import generate_random_api_key


def test_generate_random_api_key():
    api_key_pattern = re.compile(r"^[0-9a-f]{32}$")
    for _ in range(100):
        api_key = generate_random_api_key()
        assert api_key_pattern.match(api_key)
