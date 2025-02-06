import jinja2
import json
import logging
from pathlib import Path

from . import utils

logger = logging.getLogger("resume_builder")

BASE_DIR = Path(__file__).resolve().parent.parent

COMPONENTS_DIR = BASE_DIR / "components"
TECH_STACK_JSON = COMPONENTS_DIR / "tech_stack.json"
RESUME_TEX = BASE_DIR / "resume.tex"
RESUME_JSON = BASE_DIR / "config.json"


def get_tech_stack(tech_stack: dict[dict[str, int]]) -> list[str]:
    pytexs = []
    for tech in tech_stack.values():
        public_stack = filter(lambda x: x[1] == 3, tech.items())
        pytexs += [x[0] for x in public_stack]
    return sorted(pytexs) or [
        "Python",
        "SQL",
        "Terraform",
        "Kubernetes",
        "GitHub Actions",
    ]


def resume_builder():
    resume_config = utils.read_json(RESUME_JSON)
    tech_stack = utils.read_json(TECH_STACK_JSON)

    logger.info("Resume config: %s", json.dumps(resume_config, indent=2))

    latex_jinja_env = jinja2.Environment(
        block_start_string="\\BLOCK{",
        block_end_string="}",
        variable_start_string="\\VAR{",
        variable_end_string="}",
        comment_start_string="\\#{",
        comment_end_string="}",
        line_statement_prefix="%-",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(COMPONENTS_DIR),
    )

    template = latex_jinja_env.get_template("resume.tex.j2")
    content = template.render(tech_stack=get_tech_stack(tech_stack), **resume_config)

    utils.write_text(RESUME_TEX, content, encoding="utf-8")
    logger.info("Succesfully exported %s", RESUME_TEX)
