from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Proj.views import list_persons, insertForm, home,Person2add, listAll
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^logout/', auth_views.logout ,{"next_page" : "home"} ,name='logout'),
    url(r'^login/', auth_views.login ,{"template_name" : "login.html"} ,name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^insert/', Person2add ,name='insert'),
    url(r'^$', home, name='home'),
    url(r'^person/$', list_persons, name='persons'),
    url(r'^list/$', listAll, name='list'),
]
