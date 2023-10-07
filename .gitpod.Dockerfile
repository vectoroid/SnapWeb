FROM gitpod/workspace-full

RUN curl -fsSL https://deta.space/assets/space-cli.sh | sh
RUN echo 'export DETA_INSTALL="/home/gitpod/.detaspace"' >> /home/gitpod/.bashrc.d/90-detaspace &&
    echo 'export PATH="$DETA_INSTALL/bin:$PATH"' >> /home/gitpod/.bashrc.d/90-detaspace