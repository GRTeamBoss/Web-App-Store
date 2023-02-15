from django.urls import path


from .views import *


urlpatterns = [
    path('<account_name>', account, name='account')
]