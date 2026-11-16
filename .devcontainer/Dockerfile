# syntax=docker/dockerfile:1@sha256:4edf897a3ffa55b89f906fc8cc78afdb3f1834cc9c7083565e611a8a7d5fe99e

FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:81a1340fea1e72ad4a8e9a016128b0c61041cf182ea49fd788023e52842bc147

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
