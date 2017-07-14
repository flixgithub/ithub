# Blog
django blog
将django+uwsgi+nginx+mysql通过docker的方式部署到Ubuntu 16.4
## 应用部件版本：
django版本：Django (1.11.3)  
uWSGI版本： uWSGI (2.0.15)  
nginx版本:  nginx/1.10.3 (Ubuntu)  
## 操作系统版本：
NAME="Ubuntu"
VERSION="16.04.2 LTS (Xenial Xerus)"  
## 部署方式:
1. 安装操作系统，这里是16.04.2 LTS  
2. 安装docker，参考：http://www.jianshu.com/p/2e0c9ed5433d 可以安装最新的docker版本  
3. 选择一个目录下载mysql的docker镜像,https://hub.docker.com/_/mysql/ 选择(5.5/Dockerfile)，我用的是5.5的版本，直接下载Dockerfile，docker-entrypoint.sh
   这两个文件的，放在同一个目录，这里注意dockerfile里面有两个地方有认证的这一步 gpg --keyserver ha.pool.sks-keyservers.net --recv-keys ，我试了下网络原因（国内的防火墙）无法认证，我替换为了
   gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 就可以了，
   然后执行docker build -f ./mysql_dockerfile -t mysql:5.5创建mysql的 docker image，
   docker image创建完之后 docker run --name mysql -e MYSQL_ROOT_PASSWORD=root123 -d mysql:5.5， 这样mysql的docker container就创建好了  
4. 选择一个目录 比如 django-uwsgi-nginx 下载django+uwsgi+nginx, git clone https://github.com/dockerfiles/django-uwsgi-nginx.git  
   在django-uwsgi-nginx目录下下载blog项目 git clone https://github.com/flixgithub/ithub.git，覆盖一下这几个文件 nginx-app.conf supervisor-app.conf Dockerfile
   替换一下本项目中的文件  
   cp blog_dockerfile supervisor-app.conf nginx-app.conf ../django-uwsgi-nginx  
   然后bulid image, 注意 . 号不要忘了加 docker build -f blog_dockerfile -t blog:v3.0 .   
   /django-uwsgi-nginx# ls  
   app  AUTHORS  *blog_dockerfile*  Dockerfile  Dockerfile-py2  **ithub**  *nginx-app.conf*  README.md  *supervisor-app.conf*  uwsgi.ini  uwsgi_params  
   /django-uwsgi-nginx# cd ithub/  
   /django-uwsgi-nginx/ithub# ls  
   blog             comments  ithub      mysqlclient-1.3.9-cp35-cp35m-win_amd64.whl  supervisor-app.conf  uwsgi_params  
   blog_dockerfile  hubasset  manage.py  nginx-app.conf                              templates  
   bulid 结束之后启动container  
   docker run --name blog_app --link mysql:mysqldb -p 147.128.74.57:8000:8000 -d blog:v3.0  
   docker ps -a查看一下container  
   docker exec docker exec -it blog_app /bin/bash 进入container 时候lsof -i:8000看下nginx是否监听了8000端口  
 5. 浏览器访问blog http://ip:8000 （IE可能会有bootstrap方面的问题）
 6. 在 django-uwsgi-nginx/ithub 目录下运行 python3 manage.py collectstatic 来收集django的静态文件，并创建django superadmin 用户，可以用来后台管理
 7. 业务流程就是  the web client <-> the web server <-> the socket <-> uWSGI <-> Python Django  
    部署参考文档参考 https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
