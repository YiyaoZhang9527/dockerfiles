ARG name=ubuntu:18.04
FROM ${name}

LABEL author = 'MANMAN' 
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade 

# 软件安装所必须的依赖时，有可能会出现对话框进行选择，如果不选择会导致镜像制作失败，需要添加如下语句
#+++++++++++++++++++
# 添加管理员账户MANMAN，设置工作目录
RUN useradd -ms /bin/bash manman && \
    adduser manman sudo && \
    echo "manman:0"|chpasswd && \
    echo "root:0"|chpasswd

# 设置运行账户，设置环境变量并容器启动后需要运行的命令
# 改变运行账户、工作目录和运行Shell（/bin/bash，默认Shell为/bin/sh）
ENV HOME /home/manman
ENV HOSTNAME MANMAN-PC
WORKDIR /home/manman/

# 安装OpenSSH
RUN apt install -y openssh-server
# 修改ssh配置文件，文件位置/etc/ssh/sshd_config，添加允许所有主机连接，
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config && \
    echo 'sshd:ALL' >> /etc/hosts.aldlow
# 开放22端口
EXPOSE 22

ARG APT_PACKAGES="wget curl git axel "
# 下载安装 anaconda3 
ARG CONDA_DOWNLOAD_URL="https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh"
RUN apt-get update \
    && apt-get install -y --no-install-recommends ${APT_PACKAGES} \
    && axel ${CONDA_DOWNLOAD_URL} \
    && bash Miniconda3-py39_4.9.2-Linux-x86_64.sh -b -p /home/manman/miniconda3 \
    && /home/manman/miniconda3/bin/conda init
# 安装 rtsp-server 的依赖
ARG APT_PACKAGES_FOR_RTSP_SERVER_1="libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio"
ARG APT_PACKAGES_FOR_RTSP_SERVER_2="libglib2.0-dev libgstrtspserver-1.0-dev gstreamer1.0-rtsp"
ARG APT_PACKAGES_FOR_RTSP_SERVER_3="libcairo2-dev libjpeg-dev libgif-dev gcc libgirepository1.0-dev"
RUN apt-get clean \ 
    && apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends ${APT_PACKAGES_FOR_RTSP_SERVER_1} \
    && apt-get install -y --no-install-recommends ${APT_PACKAGES_FOR_RTSP_SERVER_2} \
    && apt-get install -y --no-install-recommends ${APT_PACKAGES_FOR_RTSP_SERVER_3}

# ## 安装 stitching 依赖
# ARG PIP_PACKAGES="stitching notebook matplotlib PyGObject"
# SHELL ["/home/manman/miniconda3/bin/conda", "run", "/bin/bash", "-c"]
# RUN pip install ${PIP_PACKAGES} -i https://pypi.tuna.tsinghua.edu.cn/simple 


# 设置容器运行时执行的命令，启动ssh服务,并进入bash Shell
ENTRYPOINT service ssh start && /bin/bash


# COPY source dest
# CMD ["node", "src/index.js"]