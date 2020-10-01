from django.urls import path

from .views import Login, Logout, Profile, Register

urlpatterns = [
    
    path('signUp/', Register.as_view(), name = 'signUp'),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('profile/', Profile.as_view(), name = 'profile'),  # for test only  

]
