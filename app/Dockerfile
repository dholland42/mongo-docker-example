FROM cgr.dev/chainguard/wolfi-base

RUN apk add curl gcc && curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/sbin" sh

USER nonroot

ADD --chown=nonroot:nonroot app/ /app/

WORKDIR /app

RUN uv sync

ENV PATH="$PATH:/app/.venv/bin"

CMD [ "jupyter", "notebook", "--ip", "0.0.0.0", "--port", "80" ]
