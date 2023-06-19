# Resume Builder

Sourced from: https://github.com/brndnmtthws/resume

## Overview

- `assets/`
  - contains static data used by `resume.tex`
- `components/`
  - styles resume components
  - mapped to `resume.toml` dictionary keys
- `resume_builder/`
  - Python package that:
    - iterates over `resume.toml` dictionary keys
    - reads the mapped `components` and formats the in-memory strings using `resume.toml` values (`str.format` function)
- `resume.toml`
  - each dictionary key contains a corresponding `component`
  - the keys inside nested dictionaries represent `component` values to be formatted by `resume-builder`

## Usage

```shell
git clone https://github.com/andhrelja/resume-builder
cd resume-builder
pip install .
```

Update `resume.toml` with desired values. If adding new dictionary keys, make sure to create a corresponding `components/<component>.pytex` file and add the dictionary keys to `components/main.pytex`.

## Feedback

GitHub Issues: https://github.com/andhrelja/resume-builder/issues
