from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect,JsonResponse
from django.template import loader
from .models import *
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

# Create your views here.

from rest_framework.authentication import get_authorization_header
from rest_framework.views import APIView
from rest_framework.exceptions import APIException , AuthenticationFailed

from .authentication import create_access_token, create_refresh_token , decode_access_token , decode_refresh_token
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('u_email')
        password = request.data.get('u_password')
        
        try:
            user = User.objects.get(u_email=email)
        except User.DoesNotExist:
            raise APIException('Invalid credentials!')

        if not user.check_password(password):
            raise APIException('Invalid credentials!')
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }

        return response
    
class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)

        raise AuthenticationFailed('unauthenticated')
    
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })

class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response
#


def index(request):
    objs = Item.objects.all().values()
    json_data = []
    for obj in objs:
        json_data.append(obj)

    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def all_faculties(request):
    allfaculties = Facultie.objects.all()
    serializer = FacultiesSerializer(allfaculties,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)

@api_view(['GET'])
def all_items(request):
    allitems = Item.objects.all()
    serializer = ItemsSerializer(allitems,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)

