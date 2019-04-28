# analize_sys
1. 首先需要一个Python3.6官方镜像 docker pull python:3.6.0

2. build.sh是一个简单的打包脚本，把django代码打了一个压缩包，以及管理一下镜像的名字

3. requirements.txt是python的依赖，没啥好说的

4. Dockerfile是打镜像的脚本，首先会从网上pull一个python:3.6.0镜像，在其基础上加载了analize.sys.tar.gz代码包，并安装requirements.txt中的python依赖；

工程更多介绍见https://zhanggq.github.io/post/zgq-paas-python-django/