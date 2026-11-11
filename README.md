# grawGo API

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
5. `git push --follow-tags`
