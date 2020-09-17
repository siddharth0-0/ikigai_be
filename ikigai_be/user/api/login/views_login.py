from django.shortcuts import render, redirect
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.views import status
from user.models import User
from user.serializers import userSerializer
import pdb

class login_user(APIView):


    def post(self, request):

        #pdb.set_trace()
        print(request.data)

        uemail = request.data['email']
        upassword = request.data['password']
        output_json = {}

        try:
            userInfo = User.objects.filter(email__exact=uemail).first()
            userInfo_serializer = userSerializer(userInfo, many=False)
            print("userInfo",userInfo)
            print("userInfo_serializer",userInfo_serializer)

            if userInfo_serializer.data['email'] != uemail:
                print("data not available")
                output_json['Status'] = 'Failure'
                output_json['Message'] = 'Invalid User email'
                return Response (output_json)

            elif userInfo_serializer.data['password'] != upassword:
                output_json['Status'] = 'Failure'
                output_json['Message'] = 'Wrong Password'   
                return Response (output_json)
            
            else:
                print("welcome")
                output_json['Status'] = 'Success'
                output_json['Message'] = ' User Loged In'
                return Response (output_json)

        except Exception as ex:
            print("wtf",ex) 
            output_json['Status'] = 'Failure'
            output_json['Message'] = 'Something Went Wrong ' + str(ex)
            return Response (output_json)



