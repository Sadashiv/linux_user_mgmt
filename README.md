Manage user Account in Linux Install mnaually
=============================================


This repositary is going to help AddUser, ModifyUser and DelUser in Linux only

Step 1 : clone git repo either of way you feel compfort:::
         $ git clone https://github.com/sadashivhb/linux_user_mgmt
         or
         $ git clone git@github.com:sadashivhb/linux_user_mgmt

step 2 : cd usermgmt::
         Install customized python
         $ ./installpy.sh -s
         Error: zipimport.ZipImportError: can't decompress data; zlib not available
         RHEL/CentOS: yum install wget gcc gcc-c++ zlib zlib.i686 zlib-devel zlib-devel.i686 libffi-devel xz-devel \
                      sqlite-devel python-devel openldap-devel openssl-devel bzip2-devel sqlite sqlite-devel openssl-devel.i686
         UBUNTU: apt-get install wget gcc libncursesw5-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev libssl-dev \
                 openssl zlib1g-dev libffi-dev libmysqlclient-dev libsasl2-dev python-dev libldap2-dev libbz2-dev

         Once above command execution success
         check python installed in the current working directory
         $ ./usr/bin/python

step 3:  Edit the line number 13 ==> sys_sudo_pwd = 'sudopasswd'::
         Open usermgmt/views.py
         Edit the line number 13 ==> sys_sudo_pwd = 'sudopasswd'
         sudopasswd is the password of linux user trying install usermgmt 

Step 4 : Sync the modules and migrate::
         $ ./usr/bin/python manage.py syncdb
         $ ./usr/bin/python manage.py migrate
         $ ./usr/bin/python manage.py makemigrations

step 5 : Run the server in development mode::
         $ ./usr/bin/python manage.py runserver
         Note : Default port is going to be 8000

         Try to access below url in browser
         http://localhost:8000/home

         Run with cutomized port say xxxx
         $ ./usr/bin/python manage.py runserver xxxx

         If it's not able to access into other machine open for any IP in same network
         $ ./usr/bin/python manage.py runserver 0.0.0.0:xxxx

If above step is not going to work for you::

However please install python=3.8 and Django=3.2

Once installation done please perform step no 4 and 5 Again.
============================================================

Install MySQL
=============
sudo apt install mysql-server
sudo systemctl start mysql.service
sudo systemctl status mysql.service
mysql_secure_installation 
sudo mysql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
exit
mysql -u root -p
mysql> CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
mysql> CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';

Create database:
mysql> create database djangodb;

$ ./usr/bin/python3 manage.py makemigrations usermgmt
$ ./usr/bin/python3 manage.py migrate usermgmt



Creating Docker image for our Application
=========================================
docker build -t <image_name>:<version> .

docker build -t linux_usermgmt:v1.0 .

Tag image: docker tag linux_usermgmt:v1.0 9538253250/linux_usermgmt:v1.0
Push image: docker push 9538253250/linux_usermgmt:v1.0

Docker-compose to run with django app and MySQL
===============================================
docker-compse up
