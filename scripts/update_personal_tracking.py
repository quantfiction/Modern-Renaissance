from modern_renaissance.log import logger_init
from modern_renaissance.update import execute_notebook
from modern_renaissance.utils import set_execution_path

if __name__ == "__main__":
    set_execution_path()
    execute_notebook("update_personal_tracking")
