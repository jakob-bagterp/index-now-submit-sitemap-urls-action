import sys

SUCCESS_STATUS_CODES = [200, 202]


def is_successful_response(status_code: int) -> bool:
    return status_code in SUCCESS_STATUS_CODES


def exit_with_success() -> None:
    sys.exit(0)


def exit_with_failure() -> None:
    sys.exit(1)
