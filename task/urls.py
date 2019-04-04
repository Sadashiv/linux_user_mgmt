from django.conf.urls import patterns, include, url
from django.contrib import admin
import usermgmt
from usermgmt import views

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webhook$', views.webhook, name='webhook'),
    url(r'home', views.home, name='home'),
    url(r'index', views.index, name='index'),
    url(r'addsuccess', views.addsuccess, name='addsuccess'),
    url(r'usermod', views.usermod, name='usermod'),
    url(r'modifyuser', views.modifyuser, name='modifyuser'),
    url(r'userdel', views.userdel, name='userdel'),
    url(r'deleteduser', views.deleteduser, name='deleteduser'),
    url(r'usergrant', views.usergrant, name='usergrant'),
    url(r'grantusersucc', views.grantusersucc, name='grantusersucc'),
    url(r'register', views.register, name='register'),
    url(r'login', views.user_login, name='login'),
    url(r'logout', views.user_logout, name='logout'),

)
