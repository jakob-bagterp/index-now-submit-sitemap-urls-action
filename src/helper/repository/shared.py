import os
import subprocess
from pathlib import Path

GITHUB_WORKSPACE_TOKEN = "GITHUB_WORKSPACE"

GH_PAGES_BRANCH_NAME = "gh-pages"


def get_name_of_current_git_branch() -> str:
    """Get the name of the current git branch."""

    result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
    return result.stdout.strip()


def go_to_branch(branch_name: str) -> None:
    """Attempt to switches to a branch and pull the latest changes."""

    if get_name_of_current_git_branch() == branch_name:
        subprocess.run(["git", "switch", "--create", "--track", branch_name])
    subprocess.run(["git", "pull", "origin", branch_name, "--rebase"])


def go_to_repository_root() -> None:
    """Change directory to the root of the current repository."""

    workspace_path = os.environ.get(GITHUB_WORKSPACE_TOKEN)
    if workspace_path:
        repository_root = Path(workspace_path)
        os.chdir(repository_root)
        print(f"Changed to repository root: {repository_root}")
    else:
        os.chdir(Path(__file__).parent.parent.parent)
        print("Not running in GitHub Actions environment. Using root of project directory instead.")
