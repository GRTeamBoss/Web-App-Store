from django.urls import path


from .views import *

urlpatterns = [
    path('start', registration, name='registration')
]