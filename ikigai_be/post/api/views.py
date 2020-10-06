import pdb

from post.models import Mood, Post
from post.serializers import (MoodSerializer, PostCreateUpdateSerializer,
                              PostSerializer)
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .permissions import IsOwnerOrReadOnly


class GetMoods(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        moods_var = Mood.objects.all() 
        serializer_var = MoodSerializer(moods_var, many = True)
        return Response(serializer_var.data)


class GetAllPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class CreatePost(CreateAPIView):
    # pdb.set_trace()
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class UpdatePost(RetrieveUpdateAPIView):
    # TODO only owener of the post must be able to upadate
    # pdb.set_trace()
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
