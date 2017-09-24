"""ghswebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout

from main.views import index
from admin.views import admin_index
from user.views import login
import announcements.urls as announcements
import hours.urls as hours

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^djangoadmin/', admin.site.urls),
    url(r'^admin/', admin_index, name='admin_index'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, {'next_page': '/'}, name='logout'),
    url(r'^announcements/', include(announcements)),
    url(r'^hours/', include(hours)),
    url(r'^$', index, name='index')
]
