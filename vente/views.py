import datetime

import sweetify
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from rest_framework import viewsets
from rest_framework_datatables import pagination, filters

from existing_db.models import Vendeurs, Clients
from .filters import DefaultDbWorkaroundDatatablesFilterBackend #, ExistingDbWorkaroundDatatablesFilterBackend
from .serializers import VenteSerializer, ClientSerializer

from vente.models import Vente



class IndexView(View):
    def get(self, request):
        ventes = Vente.objects.all()
        vendeurs = Vendeurs.objects.all()
        clients = Clients.objects.all()

        return render(request,
                      'vente/index.html',
                      {
                          'ventes': ventes,
                          'vendeurs': vendeurs,
                          'clients': clients,
                      })


class CreateVenteView(View):
    def post(self, request):
        date_vente = request.POST.get('date_vente',None)
        vendeur_id = request.POST.get('vendeur', None)
        client_id = request.POST.get('client', None)
        prix_de_vente = request.POST.get('prix_de_vente',None)

        # Perform the necessary logic to create the vente
        # ...
        vente = Vente.objects.create(date_vente=datetime.datetime.now(), prix_de_vente=prix_de_vente, vendeur_id=vendeur_id,
                                     client_id=client_id)
        vente.save()


        # Show success message using Django's messages framework
        sweetify.success(request, 'Success', text='Operation completed successfully', icon='success')

        response = HttpResponse()
        response["HX-Redirect"] = reverse("index")
        return response


class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer
    filter_backends = [DefaultDbWorkaroundDatatablesFilterBackend]
    pagination_class = pagination.DatatablesPageNumberPagination


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DefaultDbWorkaroundDatatablesFilterBackend]
    pagination_class = pagination.DatatablesPageNumberPagination
