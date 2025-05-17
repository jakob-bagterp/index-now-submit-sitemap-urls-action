import os
import subprocess
import time

import requests

from helper.index_now.api_key import get_api_key_file_name
from helper.repository.add_api_key_file import create_api_key_file
from helper.repository.remove_api_key_file import remove_api_key_file
from helper.repository.shared import get_name_of_current_git_branch


def test_add_and_remove_api_key_file() -> None:
    def clean_up_and_remove_latest_commits(commit_count: int, return_to_branch: str) -> None:
        subprocess.run(["git", "reset", "--hard", f"HEAD~{commit_count}"])
        subprocess.run(["git", "checkout", return_to_branch])

    def attempt_to_get_api_key_file_from_gh_pages(api_key_file_name: str, max_attempts: int = 5, wait_seconds: int = 2) -> requests.Response:
        api_key_file_url = f"https://jakob-bagterp.github.io/index-now-submit-sitemap-gh-pages-action/{api_key_file_name}"
        attempt = 1
        while attempt <= max_attempts:
            try:
                response = requests.get(api_key_file_url)
                if response.status_code == 200:
                    return response
            except Exception:
                pass
            time.sleep(wait_seconds)
            attempt += 1
        return requests.get(api_key_file_url)

    api_key = "a1b2c3d4"
    api_key_file_name = get_api_key_file_name(api_key)
    origin_branch = get_name_of_current_git_branch()

    create_api_key_file(api_key)
    assert os.path.exists(api_key_file_name)
    assert os.path.isfile(api_key_file_name)

    # TODO: Temporary prints to check if the script is working:
    print(f"{api_key_file_name=}")
    print("Current directory:", os.getcwd())
    print("Available files:", os.listdir())
    print("Current branch:", get_name_of_current_git_branch())

    with open(api_key_file_name) as file:
        assert file.read().strip() == api_key
    response = attempt_to_get_api_key_file_from_gh_pages(api_key_file_name)
    assert response.status_code == 200
    assert response.text.strip() == api_key

    remove_api_key_file(api_key)
    assert not os.path.exists(api_key_file_name)

    clean_up_and_remove_latest_commits(commit_count=2, return_to_branch=origin_branch)
