from django.db import models


# Create your models here.


# class Account(models.Model):
#     first_name = models.CharField(max_length=255)
#     second_name = models.CharField(max_length=255)
#     nickname = models.CharField(max_lenght=255, unique=True, editable=True)
#     e_mail = models.EmailField(unique=True, editable=True)
#     phone_number = models.PositiveBigIntegerField(unique=True, editable=True)
#     date_of_birth = models.DateField(default='01.01.1999', editable=True)
#     image = models.ImageField(default='/static/account/img/default.png', width_field='1920', height_field='1080')
#     password = models.TextField(max_length=800, unique=True)