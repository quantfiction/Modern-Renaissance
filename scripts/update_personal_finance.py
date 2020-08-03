import os
from pathlib import Path

from modern_renaissance.log import logger_init
from modern_renaissance.update import execute_notebook


if __name__ == "__main__":
    # cd to correct execution directory
    execution_path = Path.home() / "repositories" / "modern_renaissance"
    os.chdir(execution_path)

    # Execute notebook
    execute_notebook("update_personal_finance")
