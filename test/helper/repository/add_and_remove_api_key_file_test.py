import os
import subprocess
import time

import pytest
import requests

from helper.index_now.api_key import get_api_key_file_name
from helper.repository.add_api_key_file import create_api_key_file
from helper.repository.remove_api_key_file import remove_api_key_file
from helper.repository.shared import (GH_PAGES_BRANCH_NAME,
                                      GITHUB_WORKSPACE_TOKEN,
                                      get_name_of_current_git_branch,
                                      go_to_branch)


def clean_up_and_remove_latest_commits_from_gh_pages(commit_count: int, verify_commit_messages: list[str]) -> None:
    """Removes the latest commits from the `gh-pages` branch. This is useful for cleaning up after tests that create and remove API key files.

    Args:
        commit_count (int): The number of commits to remove.
        verify_commit_messages (list[str]): The commit messages to verify that the latest commits are, so we don't remove any wrong commits.
    """

    def get_latest_commit_messages(commit_count: int) -> list[str]:
        result = subprocess.run(["git", "log", "-n", str(commit_count), "--pretty=format:%s"], capture_output=True, text=True)
        commit_messages = result.stdout.strip().split("\n")
        return commit_messages

    def ensure_latest_commits_are_test_commits(commit_count: int, verify_commit_messages: list[str]) -> bool:
        latest_commit_messages = get_latest_commit_messages(commit_count)
        return all(commit_message in latest_commit_messages for commit_message in verify_commit_messages)

    origin_branch = get_name_of_current_git_branch()
    go_to_branch(GH_PAGES_BRANCH_NAME)
    proceed_with_reset = ensure_latest_commits_are_test_commits(commit_count, verify_commit_messages)
    if proceed_with_reset:
        subprocess.run(["git", "reset", "--hard", f"HEAD~{commit_count}"])
        subprocess.run(["git", "push", "--force", "origin", GH_PAGES_BRANCH_NAME])
    go_to_branch(origin_branch)


def attempt_to_get_api_key_file_from_gh_pages(api_key_file_name: str, timeout_seconds: int = 440, retry_seconds: int = 5) -> requests.Response:
    """It takes a while for the GitHub Pages deployment to be ready. This function will attempt to get the file from the GitHub Pages URL, and if it fails, it will wait and try again until a timeout is reached.

    Args:
        api_key_file_name (str): The name of the API key file to retrieve.
        timeout_seconds (int): The maximum time in seconds to wait for the file to be available.
        retry_seconds (int): The time interval in seconds to wait between retries.
    """

    api_key_file_url = f"https://jakob-bagterp.github.io/index-now-submit-sitemap-gh-pages-action/{api_key_file_name}"
    max_attempts = timeout_seconds // retry_seconds
    attempt = 1
    while attempt <= max_attempts:
        try:
            response = requests.get(api_key_file_url)
            if response.status_code == 200:
                return response
        except Exception:
            pass
        time.sleep(retry_seconds)
        attempt += 1
    return requests.get(api_key_file_url)


def test_add_and_remove_api_key_file() -> None:
    if not os.environ.get(GITHUB_WORKSPACE_TOKEN):
        pytest.skip("Skipping test because not running in GitHub Actions environment.")

    api_key = "a1b2c3d4"
    api_key_file_name = get_api_key_file_name(api_key)

    assert "sitemap.xml" not in os.listdir()  # Ensure that we're not in the root of GitHub Pages where the sitemap file is.

    added_api_key_commit_message = "TEST: Added API key file"
    create_api_key_file(api_key, commit_message=added_api_key_commit_message)  # This commit will trigger a deployment to GitHub Pages.
    assert os.path.exists(api_key_file_name)
    assert os.path.isfile(api_key_file_name)
    with open(api_key_file_name) as file:
        assert file.read().strip() == api_key

    assert "sitemap.xml" in os.listdir()  # Ensure that working directory is in the root that contains a known, almost static sitemap file of GitHub Pages.

    response = attempt_to_get_api_key_file_from_gh_pages(api_key_file_name)
    assert response.status_code == 200
    assert response.text.strip() == api_key

    removed_api_key_commit_message = "TEST: Removed API key file"
    remove_api_key_file(api_key, commit_message=removed_api_key_commit_message)  # This commit will trigger a deployment to GitHub Pages.
    assert not os.path.exists(api_key_file_name)

    clean_up_and_remove_latest_commits_from_gh_pages(commit_count=2, commit_messages=[added_api_key_commit_message, removed_api_key_commit_message])
