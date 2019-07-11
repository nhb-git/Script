# 编写一个Dockerfile, 使用Nginx做为基础镜像, 把任意一个静态index.html文件拷贝至Nginx的html目录中

## 准备文件

> 将dockerfile和index.html文件复制到A目录下，进入A目录

## 构建镜像

```bash
docker build -t test-nginx .
```

## 运行容器

```bash
docker run -itd --name test-nginx -p 80:80 test-nginx
```
