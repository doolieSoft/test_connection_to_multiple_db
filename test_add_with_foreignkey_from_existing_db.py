import os
import sys
import time
from pathlib import Path
from threading import Timer

import django

dir = Path(__file__).resolve().parent
# "C:/Users/c158492/ProjetBoulot/Python/LABOS/project"
sys.path.append(dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()

from existing_db.models import Vendeurs, Clients
from vente.models import Vente

if __name__ == "__main__":
    vendeurs = Vendeurs.objects.using('existing_db').all()
    clients = Clients.objects.using('existing_db').all()

    # for i in range(1, 10000):
    #     vente = Vente(date_vente=datetime.now(), vendeur=vendeurs[0], client=clients[0], prix_de_vente=1000)
    #     vente.save(using='default')

    ventes = Vente.objects.all()
    print(time.ctime())
    with open("vente.txt", mode="w") as f:
        for v in ventes:
            # print(v.vendeur)

            # vendeur = Vendeurs.objects.get(vendeur_id=v.vendeur.vendeur_id)
            # print(f" vendeur.nom : {vendeur.nom} vendeur.prenom : {vendeur.prenom} vendeur.nom : {vendeur.nom} ")
            # client = Clients.objects.get(client_id=v.client.client_id)
            f.write(
                f"id : {v.id} date_vente : {v.date_vente} vendeur : {v.vendeur.nom} client : {v.client.nom} prix_de_vent : {v.prix_de_vente}\n")
            break
    print(time.ctime())
