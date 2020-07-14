import os
import yaml


def get_settings():
    settings_path = os.path.abspath(
        os.path.join(__file__, "..", "..", "config", "settings.yaml")
    )

    with open(settings_path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
