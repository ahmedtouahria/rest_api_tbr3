from dataclasses import field, fields
from rest_framework import serializers

from tabre3.models import Motabari3

class Motabari3Serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Motabari3
        fields=['id','name','wilaya','commun','zomra','age','phone','created_on']
        extra_kwargs={
            'name':{'write_only': True},
        }