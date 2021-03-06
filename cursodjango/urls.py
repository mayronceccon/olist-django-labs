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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from aula04.views import index
from aula06.views import index as index6, edit
from aula07.views import index as index7, restrita, \
    logout_view, permission_view
from aula09.views import index9
from aula10.views import mostra_arquivo_estatico
from aula11.views import aula11


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("aula03.urls")),
    path('estatico', mostra_arquivo_estatico, name="aula10"),
    path('aula4', index),
    path('aula6', index6),
    path('aula6/<int:id>', edit),
    path('entrar', index7, name='login'),
    path('aula7/restrita', restrita),
    path('aula7/view-carrinho', permission_view),
    path('aula7/sair', logout_view, name="logout"),
    path('aula9', index9, name="aula9"),
    path('aula11', aula11, name="aula11"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
