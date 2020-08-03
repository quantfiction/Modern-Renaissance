import os
import yaml
from pathlib import Path


def get_settings():
    settings_path = os.path.abspath(
        os.path.join(__file__, "..", "..", "config", "settings.yaml")
    )

    with open(settings_path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def get_execution_path():
    """cd into the proper directory for script execution"""
    execution_path = Path.home() / "repositories" / "modern_renaissance"

    return execution_path


def set_execution_path():
    execution_path = get_execution_path()
    os.chdir(execution_path)
