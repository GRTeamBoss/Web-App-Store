from django.urls import path

from .views import *

urlpatterns = [
    path('admin', admin, name='dashboard-admin'),
    path('editor', editor, name='dashboard-editor'),
    path('advertiser', advertiser, name='dashboard-advertiser')
]