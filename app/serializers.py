from dataclasses import field
from rest_framework import serializers
from .models import  Mailing_list,Client,Message
from .models import *

class Mailing_listSerializer(serializers.ModelSerializer):

    class Meta:
        moderl = Mailing_list
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
