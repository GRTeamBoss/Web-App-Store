from django.shortcuts import render, HttpResponse

# Create your views here.

def overview(request):
    return HttpResponse('/overview/main')