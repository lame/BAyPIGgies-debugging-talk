# Debugging Talk README

## Install dependencies

1) Make sure you have python 3.8 or newer

    > ```bash
    > python --version
    > ```

2) Create a virtual environment

    > ```bash
    > python -m venv .venv
    > ```

3) Activate virtualenv

    > ```bash
    > source .venv/bin/activate
    > ```

4) Install `poetry`

    > ```bash
    > pip install poetry
    > ```

5) Install dependencies

    > ```bash
    > poetry install
    > ```

6) Your project should be runable now!

## Running the Presentation

```bash
jupyter notebook Eternal\ Sunshine\ of\ the\ Debugged\ Mind.ipynb
```

From there you can export to slides like used in the .html presentation with `file -> Download as -> Reveal.js slides (html)`

## Running the flask example

```bash
flask  --app flask_app/app.py --debug run
```
