import json
import subprocess

from .exceptions import SerienabendShefError


def get_next_chef():
    result = subprocess.run(
        ["serienabend-shef", "--format=json", "chef", "get-next"], capture_output=True
    )

    throw_on_non_zero_exit_code(result)

    return json.loads(result.stdout)


def throw_on_non_zero_exit_code(completed_process: subprocess.CompletedProcess):
    if completed_process.returncode != 0:
        stdout_parsed = json.loads(completed_process.stdout)
        error = stdout_parsed["error"]

        raise SerienabendShefError(
            "serienabend-shef exited with a non-zero code", error
        )
