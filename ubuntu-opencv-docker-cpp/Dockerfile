ARG name=ubuntu-cpp-opencv:core
FROM ${name}

LABEL author = 'MANMAN' 
ENV DEBIAN_FRONTEND=noninteractive

ENV HOME /home/manman-cpp
ENV HOSTNAME MANMAN-CPP-PC
WORKDIR /home/manman-cpp/

RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN zsh -c "source ~/.zshrc"

RUN axel https://github.com/owenthereal/ccat/releases/download/v1.1.0/linux-amd64-1.1.0.tar.gz \
    && chown +x linux-amd64-1.1.0.tar.gz \
    && tar xfz linux-amd64-1.1.0.tar.gz \
    cp linux-amd64-1.1.0/ccat /usr/local/bin/ \
    chmod +x /usr/local/bin/ccat \
    echo "alias cat='/usr/local/bin/ccat'" >> /etc/profile

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config && \
    echo 'sshd:ALL' >> /etc/hosts.aldlow
# 开放22端口
EXPOSE 22
ENTRYPOINT service ssh start; tail -f /dev/null