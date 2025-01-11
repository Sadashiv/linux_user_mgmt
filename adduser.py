import os
import crypt
import logging
import pwd
#class Pwd(object):
#    def userPasswd(self, login, password):
#        encPass = crypt.crypt(password, password)
#        command = "sudo usermod -p '{0:s}' {1:s}".format(encPass, login)
#        result = os.system(command)
#        if result != 0:
#            logging.error(command)
#        return result
#
#pp = Pwd()
#a = pp.userPasswd('sada', 'sad')

#password = 'sada'
#encpass = crypt.crypt(password, '22')

#a= os.system("sudo useradd sada -p "+encpass+" -m -s /bin/bash")
#print a
#a= os.system("sudo useradd sada -p "+encpass+" -m")
#print a
#usermod -l sadaa sada

for u in pwd.getpwall():
    print(u[0])
    if u[0] == 'sadaa':
        pass

try:
    a = pwd.getpwnam('sada')
    print(a)
except:
    print("bye")
