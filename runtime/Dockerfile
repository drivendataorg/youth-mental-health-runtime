FROM nvidia/cuda:11.8.0-base-ubuntu22.04

USER root

ARG CPU_OR_GPU=gpu

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8  \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    SHELL=/bin/bash

COPY apt.txt apt.txt
RUN apt-get update --fix-missing \
    && apt-get install -y apt-utils 2> /dev/null \
    && xargs -a apt.txt apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /apt.txt

COPY --chown=$MAMBA_USER:$MAMBA_USER pixi.lock /tmp/pixi.lock
COPY --chown=$MAMBA_USER:$MAMBA_USER pixi.toml /tmp/pixi.toml

RUN curl -fsSL https://pixi.sh/install.sh | bash
ENV PATH="/root/.pixi/bin:$PATH"
RUN pixi install --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU} && \
    pixi clean --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU}

# RUN curl -fsSL https://pixi.sh/install.sh | bash
# RUN echo "source /root/.bashrc" >> /tmp/setup
# RUN echo "pixi install --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU}" >> /tmp/setup
# RUN /bin/bash -C "tmp/setup"

# RUN /bin/bash --login -c "pixi install --manifest-path /tmp/pixi.toml -e gpu"

# RUN ["/bin/bash", "-c", "source /root/.bashrc"]
# RUN ["/bin/bash", "-c", "pixi install --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU}"]

# RUN source /root/.bashrc
# RUN pixi install --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU} && \
#     pixi clean --manifest-path /tmp/pixi.toml -e ${CPU_OR_GPU}

RUN mkdir /code_execution
RUN chown -R ${MAMBA_USER}:${MAMBA_USER} /code_execution

COPY tests /code_execution/tests
COPY entrypoint.sh /entrypoint.sh

WORKDIR /code_execution
USER ${MAMBA_USER}

CMD ["bash", "/entrypoint.sh"]
