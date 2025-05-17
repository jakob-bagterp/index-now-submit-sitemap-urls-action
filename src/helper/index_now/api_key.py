def get_api_key_file_name(api_key: str) -> str:
    """Get the name of the API key file.

    Args:
        api_key (str): The API key for IndexNow, e.g `a1b2c3d4`.

    Returns:
        str: The name of the API key file, e.g. `a1b2c3d4.txt`.
    """

    return f"{api_key}.txt"
