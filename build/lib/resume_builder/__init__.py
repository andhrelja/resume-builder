import sys
import json
import logging
from importlib.resources import files, as_file

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)

ref = files('resume_builder').joinpath('version.json')
with as_file(ref) as f:
    version_object = json.loads(f.read_text())

__version__ = version_object['version']
