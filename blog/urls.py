from django.urls import path


from .views import *



urlpatterns = [
    path('<id>', blog, name='blog')
]