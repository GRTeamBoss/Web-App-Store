from django.shortcuts import render, HttpResponse


# Create your views here.


def registration(request):
    content = {
        'title': 'Registration'
    }
    return render(request, 'registration/main.html')
    return HttpResponse('/registration/start')