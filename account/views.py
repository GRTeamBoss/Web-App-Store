from django.shortcuts import render, HttpResponse

# Create your views here.


def account(request, account_name):
    return HttpResponse(f'/account/{account_name}')