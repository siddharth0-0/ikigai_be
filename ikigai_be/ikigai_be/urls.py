from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.api.urls")),
    path('post/', include("post.api.urls")),
]
