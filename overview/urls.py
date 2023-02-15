from django.urls import path


from .views import *


urlpatterns = [
    path('main', overview, name='overview-main'),
]