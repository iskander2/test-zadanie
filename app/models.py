from django.db import models
from django.core.validators import *
from django.core.validators import RegexValidator
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Mailing_list(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    text = models.TextField(max_length=15)
    stop_datatime = models.DateTimeField()

class Client(models.Model):
    telephone = RegexValidator(regex=r'^7\d{10}$',message="Номер телефона должен быть в формате 7XXXXXXXXXX (X - цифры от 0 до 9)")
    code_regex = RegexValidator(regex=r'^\d{3}$',message="Код оператора должен состоять из трёх цифр")
    code = models.CharField(validators=[code_regex], max_length=3, unique=True)
    tage = models.CharField(max_length=25, unique=True)
    utc = models.CharField(max_length=3,)

class Message(models.Model):
    mailing_list = models.ForeignKey(Mailing_list, blank=True, on_delete=models.CASCADE, related_name='messages')
    create_datetime = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
    mailing = models.ForeignKey(Mailing_list, blank=True, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, blank=True, on_delete=models.CASCADE, related_name='messages')   

  