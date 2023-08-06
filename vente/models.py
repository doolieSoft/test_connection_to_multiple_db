from django.db import models

from existing_db.models import Vendeurs, Clients


class Vente(models.Model):
    date_vente = models.DateField(auto_now=False, auto_now_add=True)
    vendeur = models.ForeignKey(to=Vendeurs,on_delete=models.DO_NOTHING, db_constraint=False)
    client = models.ForeignKey(to=Clients, on_delete=models.DO_NOTHING, db_constraint=False)
    prix_de_vente = models.DecimalField(max_digits=10, decimal_places=2)

    def __repr__(self):
        return 'Vente: {}'.format(self.date_vente)

