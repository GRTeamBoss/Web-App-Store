from django.urls import path


from .views import *


urlpatterns = [
    path("seller/<username>", seller),
    path("category/<category>", division),
    path("product/<name>", product)
        ]
