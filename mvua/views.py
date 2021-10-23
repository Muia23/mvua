from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from .models import Home
from .serializers import HomeSerializer

class HomeAPIView(APIView):
    serializer_class = HomeSerializer        

    def get(self, request, format=None):        
        home = Home.get_all().values()
        return Response(home)
    
#@api_view()
#def home(request):    
#    weather = Home.get_all()
#    return Response({"home": weather.dayname})