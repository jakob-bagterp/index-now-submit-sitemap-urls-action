from helper.index_now.submit_sitemap import \
    get_submit_sitempa_cli_input_parameters


def test_get_submit_sitempa_cli_input_parameters() -> None:
    command = "submit_sitemap.py example.com a1b2c3d4 https://example.com/a1b2c3d4.txt https://example.com/sitemap.xml yandex"
    command_parameters = [str(paramater) for paramater in command.split(" ")]
    input = get_submit_sitempa_cli_input_parameters(command_parameters)
    assert input.host == "example.com"
    assert input.api_key == "a1b2c3d4"
    assert input.api_key_location == "https://example.com/a1b2c3d4.txt"
    assert input.sitemap_url == "https://example.com/sitemap.xml"
    assert input.endpoint == "yandex"
