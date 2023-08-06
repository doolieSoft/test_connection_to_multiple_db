"""
URL configuration for test_connection_to_multiple_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers

from vente.views import IndexView, VenteViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register(r'ventes', VenteViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('ventes/', include('vente.urls')),
    path('', IndexView.as_view(), name='index'),
]
