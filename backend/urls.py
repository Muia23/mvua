from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mvua.urls')),    
]

