import tomli
import json


def read_toml(path):
    with open(path, "rb") as f:
        return tomli.load(f)


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def read_text(path):
    with open(path, "r") as f:
        return f.read()


def write_text(path, content: str, **kwargs):
    with open(path, "w", **kwargs) as f:
        return f.write(content)
