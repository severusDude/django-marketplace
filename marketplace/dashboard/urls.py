from . import views
from django.urls import path

app_name = "dashboard"


urlpatterns = [
    path('', views.index, name="index")
]
