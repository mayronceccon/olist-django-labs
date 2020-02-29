"""cursodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from aula04.views import index as Aula04Index
from aula06.views import index as Aula06Index
from aula06.views import edit as Aula06Edit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aula03.urls')),
    path('navegador', include('sistema_navegador.urls')),
    path('aula04', Aula04Index),
    path('aula06', Aula06Index),
    path('aula06/<int:id>', Aula06Edit),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
