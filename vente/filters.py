from django.db import connections, models
from django.db.models import Subquery, Value
from rest_framework_datatables.filters import DatatablesFilterBackend

from existing_db.models import Vendeurs, Clients
from project.settings import config
from vente.models import Vente

# Get the password value from the 'database' section
username = config.get('database', 'username')
password = config.get('database', 'password')


class DefaultDbWorkaroundDatatablesFilterBackend(DatatablesFilterBackend):
    def dictfetchall(self, cursor):

        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def filter_queryset(self, request, queryset, view):
        # Get the sorting parameters from the request
        ordering = self.get_ordering(request, queryset, view)

        if ordering[0] == 'vendeur__nom':
            queryset = Vente.objects.raw(f"""SELECT tb1.id , tb1.date_vente, tb1.prix_de_vente, tb2.nom
   FROM vente_vente tb1
   LEFT JOIN (
     SELECT *
     FROM dblink('host=localhost dbname=exercices user={username} password={password}','SELECT vendeur_id, nom FROM vendeurs')
     AS tb2(vendeur_id int, nom text)
   ) AS tb2 ON tb2.vendeur_id = tb1.vendeur_id ORDER BY tb2.nom""", params=[])
            return queryset
        if ordering[0] == '-vendeur__nom':
            queryset = Vente.objects.raw(f"""SELECT tb1.id , tb1.date_vente, tb1.prix_de_vente, tb2.nom
               FROM vente_vente tb1
               LEFT JOIN (
                 SELECT *
                 FROM dblink('host=localhost dbname=exercices user={username} password={password}','SELECT vendeur_id, nom FROM vendeurs')
                 AS tb2(vendeur_id int, nom text)
               ) AS tb2 ON tb2.vendeur_id = tb1.vendeur_id ORDER BY tb2.nom desc""", params=[])
            return queryset

        # If the field doesn't require a different connection, use the default behavior
        return super().filter_queryset(request, queryset, view)

    def get_ordering_fields(self, request, view, fields):
        fields = super().get_ordering_fields(request, view, fields)
        ret = []
        for field_tuple in fields:
            if '.' in field_tuple[0]['data']:
                field_tuple[0]['data'] = field_tuple[0]['data'].split('.', 1)[0]
            ret.append(field_tuple)
        return ret
