import uuid


def generate_random_api_key() -> str:
    """Generate an API key for IndexNow.

    Returns:
        str: A 32 character hexadecimal string, e.g. `5017988d51af458491d21ecab6ed1811`.
    """

    return str(uuid.uuid4()).replace("-", "")[:32]


if __name__ == "__main__":
    print(generate_random_api_key())
