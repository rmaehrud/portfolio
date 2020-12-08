from django.urls import path
from . import views

app_name = "parsed_data"

urlpatterns = [
    path('', views.data, name='data'),
]