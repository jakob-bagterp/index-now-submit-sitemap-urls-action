import os
import subprocess

from helper.index_now.api_key import get_api_key_file_name
from helper.repository.add_api_key_file import create_api_key_file
from helper.repository.remove_api_key_file import remove_api_key_file


def test_add_and_remove_api_key_file() -> None:
    def get_name_of_current_branch() -> str:
        return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()

    def clean_up_and_remove_latest_commits(commit_count: int, return_to_branch: str) -> None:
        subprocess.run(["git", "reset", "--hard", f"HEAD~{commit_count}"])
        subprocess.run(["git", "checkout", return_to_branch])

    origin_branch = get_name_of_current_branch()

    api_key = "a1b2c3d4"
    api_key_file_name = get_api_key_file_name(api_key)
    create_api_key_file(api_key)
    assert os.path.exists(api_key_file_name)
    assert os.path.isfile(api_key_file_name)
    remove_api_key_file(api_key)
    assert not os.path.exists(api_key_file_name)

    clean_up_and_remove_latest_commits(commit_count=2, return_to_branch=origin_branch)
