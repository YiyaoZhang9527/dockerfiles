### 停止所有镜像

```bash
docker stop $(docker ps -aq) 
```

### Docker 快速删除无用（none）镜像

```bash
docker ps -a | grep "Exited" | awk '{print $1 }'|xargs docker stopn 
docker ps -a | grep "Exited" | awk '{print $1 }'|xargs docker rm
docker images|grep none|awk '{print $3 }'|xargs docker rmi
```

### 创建名为 opencv--rtsp-server-test-case 版本为 0.0.2 的镜像

```bash
docker build . -t opencv--rtsp-server-test-case:0.0.2
```

### 用名称的方式删除 `<REPOSITORY>`为 `:[opencv--rtsp-server-test-case] , <TAG>`为:[0.0.2] 的镜像

```
docker rmi opencv--rtsp-server-test-case:0.0.2
```

### 用ID的方式删除 `<IMAGE ID>` 为 [0e55de6d6b80] 的镜像

```
docker rmi 0e55de6d6b80
```

### 创建 <`REPOSITORY`> 为 :[`opencv--rtsp-server-test-case`]  TAG:[0.0.1] 的镜像

```bash
docker build . -t opencv--rtsp-server-test-case:0.0.1
```

### docker 端口映射

```
 docker run -it -p 7777:22 --name Ubuntu_rtsp_server -h MANMAN-PC opencv-rtsp-server:test
```

```
docker run --it -p 7776:22 --name ocv_rtsp_server -h MANMAN-PC opencv-rtsp-server:ssh
```

### ssh 进入 容器

```
ssh -p 7777 manman@192.168.1.13
```
