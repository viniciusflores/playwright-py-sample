help:
  just --list

sync:
  uv sync

setup:
  uv run playwright install --with-deps

test:
  export ENV=${ENV:-dev}; uv run pytest -n auto

test-dev:
  export ENV=dev; uv run pytest

test-prod:
  export ENV=prod; uv run pytest

test-ci-dev:
  export ENV=dev; uv run pytest -n auto --tracing=retain-on-failure --output=test-results/dev/

test-ci-prod:
  export ENV=prod; uv run pytest -n auto --tracing=retain-on-failure --output=test-results/prod/

codegen-dev:
  export ENV=dev; uv run playwright codegen https://duckduckgo.com/

codegen-prod:
  export ENV=prod; uv run playwright codegen https://www.google.com.br/

test-browser:
  export ENV=${ENV:-dev}; uv run pytest --headed

test-example-file:
  export ENV=${ENV:-dev}; uv run pytest src/test_example.py

test-parallel:
  export ENV=${ENV:-dev}; uv run pytest --numprocesses 2

test-firefox:
  export ENV=${ENV:-dev}; uv run pytest --browser firefox

test-debug:
  export ENV=${ENV:-dev}; PWDEBUG=1 uv run pytest -s -k

test-trace:
  export ENV=${ENV:-dev}; uv run pytest --tracing on

show-trace TRACE-PATH:
  export ENV=${ENV:-dev}; uv run playwright show-trace {{TRACE-PATH}}
