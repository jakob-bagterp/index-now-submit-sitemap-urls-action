import argparse
import os
import subprocess

from ..index_now.api_key import get_api_key_file_name
from .shared import GH_PAGES_BRANCH_NAME, go_to_branch


def remove_api_key_file(api_key: str) -> None:
    """Removes file with the API key from the root directory of the GitHub Pages repository. Assumes that the branch is `gh-pages`, and the file will be placed in the root directory, e.g. `/a1b2c3d4.txt`.

    Args:
        api_key (str): The API key for IndexNow, e.g `a1b2c3d4`.
    """

    go_to_branch(GH_PAGES_BRANCH_NAME)
    # go_to_repository_root()
    api_key_file_name = get_api_key_file_name(api_key)
    if os.path.exists(api_key_file_name):
        os.remove(api_key_file_name)
        subprocess.run(["git", "rm", "-f", api_key_file_name])
        subprocess.run(["git", "commit", "-m", "Removed API key file"])
        subprocess.run(["git", "push", "origin", GH_PAGES_BRANCH_NAME])
    else:
        print(f"API key file not found: {api_key_file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Remove a file with the API key in the root directory of the GitHub Pages repository.

        How to run the script:

            python remove_api_key_file.py a1b2c3d4

        The parameters are:

            "a1b2c3d4": API key for IndexNow.
        """)
    parser.add_argument("api_key", type=str, required=True, help="The API key for IndexNow, e.g. \"a1b2c3d4\".")
    input = parser.parse_args()
    remove_api_key_file(input.api_key)
