from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from user.serializers import UserSerializer

User = get_user_model()

import pdb


class Register(APIView):
    def post (self,request,format = 'json'):
        
        try:
            data = request.data
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status = status.HTTP_400_BAD_REQUEST
            )
        if "email" not in data or "password" not in data:
            return Response(
                'Email and password key are required', status = status.HTTP_400_BAD_REQUEST
            )
        #pdb.set_trace()
        print(data)
        
        user_serializer_var = UserSerializer(data = request.data)
        print(user_serializer_var)
        
        if user_serializer_var.is_valid():
            user = user_serializer_var.save()
            print(user)
            token = Token.objects.get_or_create(user=user)
            print("Token =",token[0].key)
            json_response = {"Token": token[0].key}
            return Response(json_response)
  
        else:
            print(user_serializer_var.errors)
            return Response(user_serializer_var.errors)



class Login(APIView):
    def post(self,request,format='json'):
        # pdb.set_trace()
        try:
            data = request.data
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status = status.HTTP_400_BAD_REQUEST
            )
        if "email" not in data or "password" not in data:
            return Response(
                'Email and password key are required', status = status.HTTP_400_BAD_REQUEST
            )
        username = request.data['email']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        print("user:",user)
        if user:
            # login(request,user) for websites maybe
            token = Token.objects.get_or_create(user=user)
            print("Token =",token[0].key)
            json_response = {"Token": token[0].key}
            return Response(json_response)
        else:
            return Response("Login unsuccefull. Try again")


class Logout(APIView):
    def get(self, request):
        try:
            print(request.user)
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        # logout(request)
        return Response({"success":"Successfully logged out."},
                    status=status.HTTP_200_OK)


class Profile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        pdb.set_trace()
        queryset = User.objects.get(email=request.user.email)
        user_serializer_var = UserSerializer(queryset)
        print(user_serializer_var.data)
        print(request.user)
        print(type(request.user))
        print(request.user.id)
        print(request.user.username)
        return Response(user_serializer_var.data)
