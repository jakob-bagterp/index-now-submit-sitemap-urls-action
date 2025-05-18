import os

from shared import clean_up_and_remove_latest_commits_from_gh_pages

from helper.index_now.api_key import get_api_key_file_name
from helper.repository.add_api_key_file import create_api_key_file
from helper.repository.remove_api_key_file import remove_api_key_file


def test_add_and_remove_api_key_file_without_online_check() -> None:
    api_key = "a1b2c3d4"
    api_key_file_name = get_api_key_file_name(api_key)

    assert "sitemap.xml" not in os.listdir()  # Ensure that we're not in the root of GitHub Pages where the sitemap file is.

    added_api_key_commit_message = "TEST: Added API key file"
    create_api_key_file(api_key, commit_message=added_api_key_commit_message)  # This commit will trigger a deployment to GitHub Pages.
    assert os.path.exists(api_key_file_name)
    assert os.path.isfile(api_key_file_name)
    with open(api_key_file_name) as file:
        assert file.read().strip() == api_key

    removed_api_key_commit_message = "TEST: Removed API key file"
    remove_api_key_file(api_key, commit_message=removed_api_key_commit_message)  # This commit will trigger a deployment to GitHub Pages.
    assert not os.path.exists(api_key_file_name)

    clean_up_and_remove_latest_commits_from_gh_pages(commit_count=2, verify_commit_messages=[added_api_key_commit_message, removed_api_key_commit_message])
