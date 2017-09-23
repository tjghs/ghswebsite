from django.conf.urls import url

from .views import create_announcement_view

urlpatterns = [
    url(r'^new/', create_announcement_view, name='create_announcement'),
]
