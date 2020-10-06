from django.urls import path

from .views import GetMoods, GetAllPosts, CreatePost, UpdatePost

urlpatterns = [
    
    path('getallPosts/', GetAllPosts.as_view(), name = 'all-posts'),
    path('createPost/', CreatePost.as_view(), name = 'create-post'),
    path('updatePost/<int:pk>/', UpdatePost.as_view(), name = 'update-post'),
    path('getMoods/', GetMoods.as_view(), name = 'Moods'),


]
