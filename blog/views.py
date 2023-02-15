from django.shortcuts import render, HttpResponse

# Create your views here.


def blog(request, id):
    return HttpResponse(f'/blog/{id}')