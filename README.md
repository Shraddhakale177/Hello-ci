# hello-ci

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
ruff format .
ruff check .
mypy app
pytest -q
python -m app.main
