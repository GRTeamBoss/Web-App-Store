from django.urls import path


from .views import *


urlpatterns = [
    path('auth', login, name='login-auth')
]