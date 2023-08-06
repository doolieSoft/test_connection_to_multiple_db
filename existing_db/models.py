# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class NamedForeignKey(models.ForeignKey):
    suffix_idname = 'id'
    def __init__(self, *args, **kwargs):
        suffix_idname = kwargs.pop('suffix_idname', None)
        if suffix_idname:
            self.suffix_idname = suffix_idname
        super().__init__(*args, **kwargs)

    def get_attname(self):
        return '%s_%s' % (self.name, self.suffix_idname)


class Adresses(models.Model):
    adresse_id = models.AutoField(primary_key=True)
    adresse = models.CharField(max_length=50)
    cp = models.SmallIntegerField()
    localite = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    mail = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adresses'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    categorie = models.CharField(max_length=6)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adr = NamedForeignKey(to=Adresses, on_delete=models.DO_NOTHING, suffix_idname='')

    class Meta:
        managed = False
        db_table = 'clients'


class Types(models.Model):
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'types'


class Vendeurs(models.Model):
    vendeur_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adr = NamedForeignKey(to=Adresses, on_delete=models.DO_NOTHING, suffix_idname='')

    def __repr__(self):
        return 'Vendeurs (%s)' %self.vendeur_id

    class Meta:
        app_label='existing_db'
        managed = False
        db_table = 'vendeurs'


class Voitures(models.Model):
    art_id = models.AutoField(primary_key=True)
    marque = models.CharField(max_length=20)
    modele = models.CharField(max_length=30)
    type_id = NamedForeignKey(to=Types, on_delete=models.DO_NOTHING, suffix_idname='')
    annee_modele = models.IntegerField()
    couleur = models.CharField(max_length=20)
    kilometrage = models.IntegerField()
    prix = models.IntegerField()
    vendeur = NamedForeignKey(to=Vendeurs, on_delete=models.DO_NOTHING, suffix_idname='')

    class Meta:
        managed = False
        db_table = 'voitures'
