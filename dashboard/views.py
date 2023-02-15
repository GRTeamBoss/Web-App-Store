from django.shortcuts import render, HttpResponse


# from models import *
# Create your views here.


def admin(requests):
    return HttpResponse('/dashboard/admin')


def editor(requests):
    return HttpResponse('/dashboard/editor')


def advertiser(requests):
    return HttpResponse('/dashboard/advertiser')