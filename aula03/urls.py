from django.urls import path
from . import views

app_name = "aula03"

urlpatterns = [
    path('', views.index),
    path('cookie', views.setacookie),
    path('dev.to', views.redireciona),
    path('code/<int:code>', views.show_code),
    path('<int:code>', views.http_cat),
    path('get', views.show_get_values),
    path('post', views.show_post_values),
]
