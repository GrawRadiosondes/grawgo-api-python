# syntax=docker/dockerfile:1@sha256:572cebbc2b15e6f84c077742952674889cb63cd5e9b80abdffcbe587b6f19183

FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:da0f1f04404173d7d2fa158112e09624d5a80262efa86c89882b68389dfd44eb

ENV DEBIAN_FRONTEND=noninteractive
ENV UV_LINK_MODE=copy

ENV PYTHONDONTWRITEBYTECODE="1"
ENV PYTHONUNBUFFERED="1"
ENV PYTHONPATH="src"

ENV UV_PROJECT_ENVIRONMENT="/opt/.venv"
ENV PATH="/opt/.venv/bin:$PATH"

RUN apt update && apt install -y --no-install-recommends \
    git \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

RUN git config --global submodule.recurse true
RUN git config --global pull.rebase true
RUN git config --global rebase.autoStash true

#RUN mkdir -p -m 0600 ~/.ssh
#RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN uv tool update-shell
RUN uv tool install bump-my-version
RUN uv tool install ruff
RUN uv tool install pytest

CMD ["sleep", "infinity"]
