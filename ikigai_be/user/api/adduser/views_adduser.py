from django.shortcuts import render, redirect
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.views import status
from user.serializers import userSerializer
import pdb


class add_user(APIView):
    def post (self,request,format = 'json'):
        
        pdb.set_trace()
        print(request.data)
        
        user_serializer_var = userSerializer(data = request.data)
        print(user_serializer_var.initial_data)

        if user_serializer_var.is_valid():
            user_serializer_var.save()

            return Response ("Registration Succefull. Welcome To Ikigai")

        return Response("Registration unsuccefull. Try again")

        # another way of writing
        # user_detail_var = {}

        # user_detail_var['name'] = request.Post.get("name")
        # user_detail_var['email'] = request.Post.get("email")
        # user_detail_var['password'] = request.Post.get("password")
        # user_detail_var['privacy_id'] = 2

        # user_serializer_var = userSerializer(data = user_detail_var)
        # print(user_serializer_var.initial_data)

        # if user_serializer_var.is_valid():
        #     user_serializer_var.save()

        #     return Response ("Registration Succefull. Welcome To Ikigai")


        # input_json = request
        # output_json = {}

        # try:
        #     user_detail_var = dict(['name', 'email' , 'passsword', 'privacy_id'],
        #     [input_json['name'],
        #     input_json['email'],
        #     input_json['password']])
            
        #     reg_input['added_by'] = str(reg_input['email_id'])
        #     reg_input['last_modified_by'] = str(reg_input['email_id'])
        #     return reg_input

