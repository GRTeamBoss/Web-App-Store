from django.shortcuts import render, HttpResponse

# Create your views here.


def statistic(request):
    return HttpResponse("/statistic/main")