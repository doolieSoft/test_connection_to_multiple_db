from django.db import connections
from rest_framework import serializers

from existing_db.models import Clients, Vendeurs
from vente.models import Vente


class ClientSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    prenom = serializers.CharField()

    class Meta:
        model = Clients
        fields = ['nom', 'prenom']


class VendeurSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    prenom = serializers.CharField()

    class Meta:
        model = Vendeurs
        fields = ['nom', 'prenom']


class VenteSerializer(serializers.ModelSerializer):
    # vendeur_nom = serializers.CharField(source='vendeur.nom')
    client = ClientSerializer()
    vendeur = VendeurSerializer()
    prix_de_vente = serializers.IntegerField()

    class Meta:
        model = Vente
        fields = ['date_vente', 'prix_de_vente', 'vendeur', 'client']
