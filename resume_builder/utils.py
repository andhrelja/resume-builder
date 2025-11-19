import json


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def write_text(path, content: str, **kwargs):
    with open(path, "w", **kwargs) as f:
        return f.write(content)
