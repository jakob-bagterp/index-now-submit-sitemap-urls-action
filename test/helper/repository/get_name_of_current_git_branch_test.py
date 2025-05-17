import subprocess

from helper.repository.shared import get_name_of_current_git_branch


def test_get_name_of_current_git_branch() -> None:
    origin_branch = get_name_of_current_git_branch()
    master_branch_name = "master"
    subprocess.run(["git", "checkout", master_branch_name])
    assert get_name_of_current_git_branch() == master_branch_name
    subprocess.run(["git", "checkout", origin_branch])  # Return to original branch to avoid side effects for other tests.
