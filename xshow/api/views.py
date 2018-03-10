from rest_framework.generics import (ListAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView)
from xshow.models import *
from .serializers import UserSerializer,UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt



class UserView(ListAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer

class GetUser(RetrieveAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer
	lookup_field='UserId'
	lookup_url_kwarg="userid"

class UpdateUser(UpdateAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer
	lookup_field='UserId'
	lookup_url_kwarg="userid"

class DestroyUser(DestroyAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer
	lookup_field='UserId'
	lookup_url_kwarg="userid"

class AddUser(CreateAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer

class UserLoginAPIView(APIView):
	serializer_class=UserLoginSerializer
	def post(self,request,*args,**kwargs):
		data=request.data
		serializer=UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data=serializer.data
			return Response(new_data,status=HTTP_200_OK)
		else:
			return Response(serializer.erros,HTTP_400_BAD_REQUEST)



