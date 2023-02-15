from django.urls import path


from .views import *

urlpatterns = [
    path('main', statistic, name="statistic-main")

]