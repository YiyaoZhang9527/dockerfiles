ARG name=kalilinux/kali-rolling
FROM ${name}

LABEL author = 'Magic'
ENV DEBIAN_FRONTEND=noninteractive

# 设置运行账户，设置环境变量并容器启动后需要运行的命令
# 改变运行账户、工作目录和运行Shell（/bin/bash，默认Shell为/bin/sh）
ENV HOME /home/magic
ENV HOSTNAME Magic-PC
WORKDIR /home/magic/

RUN apt-get -y --no-install-recommends update && apt-get -y --no-install-recommends upgrade 
RUN apt-get -y --no-install-recommends  dist-upgrade && apt-get -y autoremove && apt-get clean
ARG APT_PACKAGES="wget curl git axel python3-pip nodejs npm zsh"
RUN apt-get install -y --no-install-recommends ${APT_PACKAGES}

RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN zsh -c "source ~/.zshrc"

ARG APT_PACKAGES_BASE="curl wget vim git net-tools whois netcat-traditional pciutils usbutils axel"
ARG APT_PACKAGES_TOP10="kali-tools-top10 exploitdb man-db dirb nikto wpscan uniscan lsof apktool dex2jar ltrace strace binwalk"
ARG APT_PACKAGES_PROXY="tor proxychains"
RUN apt install -y --no-install-recommends ${APT_PACKAGES_BASE} \
    && apt install -y --no-install-recommends ${APT_PACKAGES_TOP10} \
    && apt install -y --no-install-recommends ${APT_PACKAGES_PROXY}

ARG APT_PACKAGES_TOOLS="htop "
RUN apt install -y --no-install-recommends ${APT_PACKAGES_TOOLS} 

RUN echo LANG="zh_CN.UTF-8" >> /etc/default/locale
RUN sed -i '$a\alias python="/usr/bin/python3"' ~/.zshrc

ENTRYPOINT ["/bin/zsh"]