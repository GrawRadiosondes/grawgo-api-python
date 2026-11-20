# grawGo API

Python client for the grawGo API, published to the internal package index
`https://pypi.app.graw-ops.com` (credentials: `reader` account, see app-hosting `pypi/README.md`).

## Install

```toml
[[tool.uv.index]]
name = "graw"
url = "https://pypi.app.graw-ops.com/simple/"
explicit = true

[tool.uv.sources]
grawgo = { index = "graw" }
```

Credentials come from `UV_INDEX_GRAW_USERNAME` / `UV_INDEX_GRAW_PASSWORD` (in GitHub Actions: org
secret `UV_INDEX_GRAW_PASSWORD`).

## Usage

```python
from grawgo.api import Api

api = Api(
    base_url="https://example.com/api",
    username="user@domain.tld",
    password="password",
    timeout=30,
)
```

`timeout` is the number of seconds to wait for the server on every request (default `30`). If the
server doesn't answer in time, `requests` raises a `requests.exceptions.Timeout`.

## Release

1. `ruff format`
2. `mypy -p grawgo`
3. `uv run pytest`
4. `bump-my-version`
5. `git push --follow-tags` (the tag triggers `.github/workflows/publish.yml`)
