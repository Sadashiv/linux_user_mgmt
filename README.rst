============================
Manage user Account in Linux
============================

This repositary is going to help AddUser, ModifyUser and DelUser in Linux only

Step 1 : clone git repo either of way you feel compfort:::
         $ git clone https://github.com/sadashivhb/linux_user_mgmt
         or
         $ git clone git@github.com:sadashivhb/linux_user_mgmt

step 2 : cd usermgmt::
         Install customized python
         $ ./installpy.sh -s
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

However please install python=2.7.9 and Django=1.7.5.

============================================================================================================================
Once installation done please perform step no 4 and 5 Again.
============================================================================================================================
