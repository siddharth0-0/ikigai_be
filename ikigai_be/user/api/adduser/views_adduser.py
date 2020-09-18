from django.shortcuts import render, redirect
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.views import status
from user.serializers import userSerializer
import pdb


class add_user(APIView):
    def post (self,request,format = 'json'):
        pdb.set_trace()

        input_json = request.data
        user_detail_var = {
            'name': input_json['name'],
            'email': input_json['email'],
            'password': input_json['password'],
            'privacy_id': 2,
        }

        user_serializer_var = userSerializer(data = user_detail_var)
        print(user_serializer_var.initial_data)

        if user_serializer_var.is_valid():
            user_serializer_var.save()
            return Response ("Registration Succefull. Welcome To Ikigai")

        return Response("Something Went Wrong. Kindly register Again")

