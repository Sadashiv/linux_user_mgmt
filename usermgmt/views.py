from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from usermgmt.forms import Adduser, Usermod, Userdel, UserGrantAccess, UserForm
from usermgmt.models import UserDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from usermgmt.models import UserProfile
import  pwd
import crypt
import os
import sys
import grp
# Create your views here.

sys_sudo_pwd = 'devops'


def autofetch(request):
    """ """
    username = request.POST.get('username')
    location = request.POST.get('location')
    get_data = UserDetails.objects.filter(username=username).filter(location=location)

    context_dict = {'get_data': get_data}
    return render(request, 'usermgmt/autofetch.html', context_dict)


def home(request):
    """ """
    bgcolor = os.getenv('APP_COLOR')
    print(bgcolor)
    context_dict = {'bgcolor': bgcolor}
    return render(request, 'usermgmt/home.html', context_dict)
@csrf_exempt
@login_required
def index(request):
    adduser = Adduser()


    context_dict = {'add_user' : adduser}
    return render(request, 'usermgmt/index.html', context_dict)


@csrf_exempt
@login_required
def addsuccess(request):
    """ """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        shelltype = request.POST.get('shelltype')
        userexist = None
        for user in pwd.getpwall():
            if user[0] == username:
                userexist =  username
                break
        password = password
        encpass = crypt.crypt(password, '22')
        usercheck = os.system("echo "+sys_sudo_pwd+"  | sudo useradd "+username+" -p "+encpass+" -m -s /bin/bash")
        if userexist == username:
           print("User already exist: %s" %username)
        else:
           print("User Doesn't exist in the server")
           print("Creating the User: %s" %username)


    return render(request, 'usermgmt/addsuccess.html', {'userexist': userexist, 'username': username})

@csrf_exempt
@login_required
def usermod(request):
    """ """
    adduser = Usermod()

    context_dict = {'user_mod' : adduser}
    return render(request, 'usermgmt/usermod.html', context_dict)

@csrf_exempt
@login_required
def modifyuser(request):
    """ """
    if request.method == 'POST':
        old_username = request.POST.get('old_username')
        new_username = request.POST.get('new_username')
        for user in pwd.getpwall():
            if user[0] == old_username:
                oldusername = old_username
                break
        user_modify= os.system("echo "+sys_sudo_pwd+" | sudo usermod -l "+new_username+" "+old_username+"")
        group_modify= os.system("echo "+sys_sudo_pwd+" | sudo groupmod -n "+new_username+" "+old_username+"")
        if user[0] == old_username:
            oldusername = old_username
            new_username = new_username
        else:
            oldusername = None

    return render(request, 'usermgmt/usermodsucc.html', {'new_username': new_username, 'oldusername': oldusername})


@csrf_exempt
@login_required
def userdel(request):
    """ """
    userdel = Userdel()

    context_dict = {'user_del' : userdel}
    return render(request, 'usermgmt/userdel.html', context_dict)


@csrf_exempt
@login_required
def deleteduser(request):
    """ """
    if request.method == 'POST':
        username = request.POST.get('username')
        for user in pwd.getpwall():
            if user[0] == username:
                username = username
                break
        user_logged = os.system("who | cut -d' ' -f1 | sort | uniq > user.txt")
        fr = open('user.txt', 'r')
        for userlog in fr:
            if userlog == username:
                return userlog
        fr.close()
        user_delete = os.system("echo "+sys_sudo_pwd+" | sudo userdel -r "+username+"")
        group_delete = os.system("echo "+sys_sudo_pwd+" | sudo groupdel "+username+"")
        if user[0] == username:
            username = username
        else:
            username = None

    return render(request, 'usermgmt/userdelsucc.html', {'username': username, 'userlog': userlog})

@csrf_exempt
@login_required
def usergrant(request):
    """ """
    usergrant = UserGrantAccess()

    context_dict = {'user_grant' : usergrant}
    return render(request, 'usermgmt/usergrant.html', context_dict)

@csrf_exempt
@login_required
def grantusersucc(request):
    """ """
    if request.method == 'POST':
        username = request.POST.get('username')
        for user in pwd.getpwall():
            if user[0] == username:
                username = username
                break

        if user[0] == username:
            username = username
            get_sudoers_file = os.system("echo "+sys_sudo_pwd+"| sudo cp /etc/sudoers .")
            get_sudo_tmp = os.system("echo "+sys_sudo_pwd+" | sudo cp sudoers sudoers.tmp")
            change_permission = os.system("echo "+sys_sudo_pwd+" | sudo chmod 777 sudoers")
            grant_sudo_access = '%s ALL=(ALL) ALL' %username
            print(grant_sudo_access)
            with open('sudoers', 'a') as fr:
                fr.write('\n')
                fr.write(grant_sudo_access)
            read_only_permission = os.system("echo "+sys_sudo_pwd+" | sudo chmod 044 sudoers")
            get_sudo_access = os.system("echo "+sys_sudo_pwd+" | sudo cp sudoers /etc/sudoers")
        else:
            username = None

    return render(request, 'usermgmt/usergrantsucc.html', {'username': username})

@csrf_exempt
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        website = request.POST.get('website')
                # Check duplicates
        if User.objects.filter(username=username).exists():
            error = "Username already taken."
        elif User.objects.filter(email=email).exists():
            error = "Email already registered."
        else:
            # Step 1 — create user in auth_user table
            user = User.objects.create_user(
                username = username,
                email    = email,
                password = password,
            )

            # Step 2 — create userprofile with website  ✅
            UserProfile.objects.create(
                user    = user,
                website = website
            )

            registered = True
        return render(request, 'usermgmt/register.html', {'registered': True})
    else:

        return render(request,
            'usermgmt/register.html' )



@csrf_exempt
def user_login(request):
   #If the request is HTTP POST, try to pull out the relevent information
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password=password)
      if user:
          #Is the account active? It could have disabled
          if user.is_active:
              # If the account is valid and active, we can login the user in
              # We'll send the user bact to the homepage
              login(request, user)
              if 'next' in request.POST:
                return HttpResponseRedirect(request.POST.get('next'))
              else:
                return HttpResponseRedirect('.')
          else:
              # An active account was used - no logging in
              return HttpResponse("Your account got disabled")
      else:
          # Bad login details were provided, So we can't log the user in
          print("Invalid login details: {0}, {1}".format(username, password))
          return HttpResponse("Invalid login details supplied.")
   # This scenario would most likely be a HTTP GET.
   else:
      # No context variables to pass to the template system, hence the
      # blank dictionay object...
      return render(request, 'usermgmt/login.html')

def user_logout(request):
    logout(request)

    #Take the user back to the homepage
    return HttpResponseRedirect('.')

