import os
import subprocess

import pytest

from helper.repository.shared import (GITHUB_WORKSPACE_TOKEN,
                                      get_name_of_current_git_branch)


def test_get_name_of_current_git_branch() -> None:
    if not os.environ.get(GITHUB_WORKSPACE_TOKEN):
        pytest.skip("Skipping test because not running in GitHub Actions environment.")

    origin_branch = get_name_of_current_git_branch()
    master_branch_name = "master"
    subprocess.run(["git", "checkout", master_branch_name])
    assert get_name_of_current_git_branch() == master_branch_name
    subprocess.run(["git", "checkout", origin_branch])  # Return to original branch to avoid side effects for other tests.
