from django.urls import path

from .views import Api, Api1


app_name = "api"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api1/', Api.as_view()),
    path('api2/', Api1.as_view())
]