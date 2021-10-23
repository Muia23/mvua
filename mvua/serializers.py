from django.db import models
from django.db.models import fields
from django.db.models.query_utils import Q
from rest_framework import serializers
from .models import Home


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Home
        fields = ['id','dayname','dayweatherlogo','rainamount','dayweathertext','daytemp']
        