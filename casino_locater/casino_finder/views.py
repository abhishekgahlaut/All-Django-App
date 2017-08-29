from django.shortcuts import render
from casino_finder.models import Casino
from casino_finder.user_models import User
from casino_finder.serializers import CasinoSerializer
from casino_finder.serializers import UserSerializer
from rest_framework import generics
from rest_framework_swagger.views import get_swagger_view
from auditable.views import AuditableMixin
from django.http import HttpResponse

schema_view = get_swagger_view(title='Casino API')

# Create your views here.



class ListCreateCasinos(AuditableMixin,generics.ListCreateAPIView):
	queryset = Casino.objects.all()
	serializer_class = CasinoSerializer

class ListCreateUser(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

