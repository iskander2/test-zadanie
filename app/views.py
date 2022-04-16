from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing_list.objects.all()
    serializer_class = Mailing_listSerializer



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer        

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer    