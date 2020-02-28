from django.urls import path
from . import views

app_name = "sistema_navegador"

urlpatterns = [
    path('', views.index)
]
