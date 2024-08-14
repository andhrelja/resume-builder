import json
import logging
from pathlib import Path

from . import utils

logger = logging.getLogger("resume_builder")

BASE_DIR = Path(__file__).resolve().parent.parent
COMPONENTS_DIR = BASE_DIR / "components"
MAIN_COMPONENT = COMPONENTS_DIR / "main.pytex"

RESUME_TOML = BASE_DIR / "resume.toml"
RESUME_TEX = BASE_DIR / "resume.tex"


def format_professional_experience(professional_experiences, pytex):
    pytexs = []
    for exp in professional_experiences:
        project_involvement = r"\item " + r"\item ".join(
            map(lambda x: x + "\n\t\t", exp["project_involvement"])
        )
        exp["project_involvement"] = project_involvement
        pytexs.append(pytex.format(**exp))
    return pytexs


def format_languages(languages, content):
    languages = "\n\t".join(
        ("{}: {}".format(lang, level) for lang, level in languages.items())
    )
    return content.format(languages=languages)


def populate_contents(resume_config):
    contents = resume_config.pop("author")
    for key, kwargs in resume_config.items():
        with open(COMPONENTS_DIR / (key + ".pytex"), "r") as f:
            content = f.read()
        if key == "professional_experience":
            contents[key] = "\n".join(format_professional_experience(kwargs, content))
        elif key == "languages":
            contents[key] = format_languages(kwargs, content)
        else:
            contents[key] = content.format(**kwargs)
    return contents


def resume_builder():
    resume_config = utils.read_toml(RESUME_TOML)
    main_component = utils.read_text(MAIN_COMPONENT)

    logger.info("Resume config: %s", json.dumps(resume_config, indent=2))

    contents = populate_contents(resume_config)
    resume_content = main_component.format(**contents)

    utils.write_text(RESUME_TEX, resume_content, encoding="utf-8")
    logger.info("Succesfully exported %s", RESUME_TEX)
