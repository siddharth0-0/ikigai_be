from django.urls import path

from .views import UserLogin, UserLogout, UserRegister, UserProfile

urlpatterns = [
    
    path('signUp/', UserRegister.as_view(), name = 'signUp'),
    path('login/', UserLogin.as_view(), name = 'login'),
    path('logout/', UserLogout.as_view(), name = 'logout'),
    path('profile/', UserProfile.as_view(), name = 'profile'),  # for test only

]
