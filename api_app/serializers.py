from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length= 50)
    course = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    
    class Meta:
        model = Student
        fields = ('__all__')
        