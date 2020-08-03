import logging
import logging.config
import os
from pathlib import Path
import yaml

from modern_renaissance.utils import get_execution_path, set_execution_path

# cd to correct execution directory
# execution_path = Path.home() / "repositories" / "modern_renaissance"
# os.chdir(execution_path)
set_execution_path()

# path = os.path.abspath(
#     os.path.join(__file__, "..", "..", "..", "config", "logger_config.yaml")
# )
config_path = get_execution_path() / "config" / "logger_config.yaml"
with open(config_path, "r") as stream:
    try:
        logging_config = yaml.load(stream, Loader=yaml.FullLoader)

    except yaml.YAMLError:
        print("Error Loading Logger Config")

# Load Logging configs
logging.config.dictConfig(logging_config)
logging.addLevelName(22, "START")
logging.addLevelName(44, "COMPLETE")
