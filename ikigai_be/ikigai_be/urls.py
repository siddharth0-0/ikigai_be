from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from user.api.adduser.views_adduser import add_user

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signUp/$',add_user.as_view()),
]
