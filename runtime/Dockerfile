FROM ghcr.io/prefix-dev/pixi:0.26.1-bookworm-slim

USER root

ARG CPU_OR_GPU=gpu

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8  \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    SHELL=/bin/bash

# Create user andset permissions
ENV RUNTIME_USER=runtimeuser
ENV RUNTIME_UID=1000
ENV RUNTIME_GID=1000

RUN echo "Creating ${RUNTIME_USER} user..." \
    && groupadd --gid ${RUNTIME_GID} ${RUNTIME_USER}  \
    && useradd --create-home --gid ${RUNTIME_GID} --no-log-init --uid ${RUNTIME_UID} ${RUNTIME_USER}

COPY apt.txt apt.txt
RUN apt-get update --fix-missing \
    && apt-get install -y apt-utils 2> /dev/null \
    && xargs -a apt.txt apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /apt.txt

COPY --chown=$RUNTIME_USER:$RUNTIME_USER pixi.lock /tmp/pixi.lock
COPY --chown=$RUNTIME_USER:$RUNTIME_USER pixi.toml /tmp/pixi.toml
RUN pixi install --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU} && \
    pixi clean --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU}

RUN mkdir /code_execution
RUN chown -R ${RUNTIME_USER}:${RUNTIME_USER} /code_execution

COPY tests /code_execution/tests
COPY entrypoint.sh /entrypoint.sh

WORKDIR /code_execution
USER ${RUNTIME_USER}

CMD ["bash", "/entrypoint.sh"]
