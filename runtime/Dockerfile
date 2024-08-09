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

# Set up code execution working directory
RUN mkdir /code_execution
RUN chown -R ${RUNTIME_USER}:${RUNTIME_USER} /code_execution
WORKDIR /code_execution

# Switch to runtime user
USER ${RUNTIME_USER}

COPY pixi.lock ./pixi.lock
COPY pixi.toml ./pixi.toml

RUN pixi install -e ${CPU_OR_GPU} --frozen \
    && rm -rf /home/${RUNTIME_USER}/.cache/

COPY entrypoint.sh /entrypoint.sh
COPY --chown=${RUNTIME_USER}:${RUNTIME_USER} tests ./tests

CMD ["bash", "/entrypoint.sh"]
