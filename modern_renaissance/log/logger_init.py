import logging
import logging.config
import os
import yaml


path = os.path.abspath(
    os.path.join(__file__, "..", "..", "..", "config", "logger_config.yaml")
)
with open(path, "r") as stream:
    try:
        logging_config = yaml.load(stream, Loader=yaml.FullLoader)

    except yaml.YAMLError as exc:
        print("Error Loading Logger Config")

# Load Logging configs
logging.config.dictConfig(logging_config)
logging.addLevelName(22, "START")
logging.addLevelName(44, "COMPLETE")
