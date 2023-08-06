from django.urls import path

from vente.views import CreateVenteView

urlpatterns = [
    path('add/',CreateVenteView.as_view(),name='add-vente'),
]