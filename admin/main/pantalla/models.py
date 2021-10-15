# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Budget(models.Model):
    id_budget = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'budget'


class Catalogue(models.Model):
    id_catalogue = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'catalogue'


class CatalogueDetail(models.Model):
    id_catalogue_detail = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_catalogue = models.ForeignKey(Catalogue, models.CASCADE, db_column='id_catalogue')

    class Meta:
        managed = False
        db_table = 'catalogue_detail'


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    dni = models.CharField(max_length=32, unique=True)
    id_legal_client_type = models.ForeignKey('LegalClientType', models.CASCADE, db_column='id_legal_client_type')
    id_client_type = models.ForeignKey('ClientType', models.CASCADE, db_column='id_client_type')
    id_budget = models.ForeignKey(Budget, models.CASCADE, db_column='id_budget')

    class Meta:
        managed = False
        db_table = 'client'


class ClientType(models.Model):
    id_client_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'client_type'


class Delimiter(models.Model):
    id_delimiter = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'delimiter'


class Destination(models.Model):
    id_destination = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'destination'


class DestinationService(models.Model):
    id_destination = models.ForeignKey(Destination, models.CASCADE, db_column='id_destination')
    id_service = models.ForeignKey('Service', models.CASCADE, db_column='id_service')
    id_destination_service = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'destination_service'


class KeyActivity(models.Model):
    id_key_activity = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'key_activity'


class LegalClientType(models.Model):
    id_legal_client_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'legal_client_type'


class Media(models.Model):
    id_media = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_media_type = models.ForeignKey('MediaType', models.CASCADE, db_column='id_media_type')
    id_destination_service = models.ForeignKey(DestinationService, models.CASCADE, db_column='id_destination_service')

    class Meta:
        managed = False
        db_table = 'media'


class MediaType(models.Model):
    id_media_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'media_type'


class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_playlist_state = models.ForeignKey('PlaylistState', models.CASCADE, db_column='id_playlist_state')
    id_destination_service = models.ForeignKey(DestinationService, models.CASCADE, db_column='id_destination_service')

    class Meta:
        managed = False
        db_table = 'playlist'


class PlaylistState(models.Model):
    id_playlist_state = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'playlist_state'


class Promo(models.Model):
    id_promo = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'promo'


class PromoDetail(models.Model):
    id_promo_detail = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_promo = models.ForeignKey(Promo, models.CASCADE, db_column='id_promo')

    class Meta:
        managed = False
        db_table = 'promo_detail'


class Purpouse(models.Model):
    id_purpouse = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'purpouse'


class Quote(models.Model):
    id_quote = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_quote_state = models.ForeignKey('QuoteState', models.CASCADE, db_column='id_quote_state')
    id_client = models.ForeignKey(Client, models.CASCADE, db_column='id_client')
    id_agent_user = models.ForeignKey('User', models.CASCADE, db_column='id_agent_user')
    id_travelexper_user = models.BigIntegerField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'quote'


class QuoteDetail(models.Model):
    id_quote_detail = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_quote = models.ForeignKey(Quote, models.CASCADE, db_column='id_quote')
    id_promo = models.ForeignKey(Promo, models.CASCADE, db_column='id_promo')

    class Meta:
        managed = False
        db_table = 'quote_detail'


class QuoteState(models.Model):
    id_quote_state = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_destination_service = models.ForeignKey(DestinationService, models.CASCADE, db_column='id_destination_service')

    class Meta:
        managed = False
        db_table = 'quote_state'


class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_budget = models.ForeignKey(Budget, models.CASCADE, db_column='id_budget')
    id_service_type = models.ForeignKey('ServiceType', models.CASCADE, db_column='id_service_type')

    class Meta:
        managed = False
        db_table = 'service'


class ServiceDetail(models.Model):
    id_service_detail = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_service = models.ForeignKey(Service, models.CASCADE, db_column='id_service')
    id_delimiter = models.ForeignKey(Delimiter, models.CASCADE, db_column='id_delimiter')
    id_travle_ritm = models.ForeignKey('TravelRitm', models.CASCADE, db_column='id_travle_ritm')
    id_purpouse = models.ForeignKey(Purpouse, models.CASCADE, db_column='id_purpouse')
    id_key_activity = models.ForeignKey(KeyActivity, models.CASCADE, db_column='id_key_activity')

    class Meta:
        managed = False
        db_table = 'service_detail'


class ServiceSupplier(models.Model):
    id_service = models.ForeignKey(Service, models.CASCADE, db_column='id_service')
    id_supplier = models.ForeignKey('Supplier', models.CASCADE, db_column='id_supplier')

    class Meta:
        managed = False
        db_table = 'service_supplier'


class ServiceType(models.Model):
    id_service_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'service_type'


class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    id_supplier_type = models.ForeignKey('SupplierType', models.CASCADE, db_column='id_supplier_type')

    class Meta:
        managed = False
        db_table = 'supplier'


class SupplierType(models.Model):
    id_supplier_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'supplier_type'


class TravelRitm(models.Model):
    id_travel_ritm = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'travel_ritm'


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'user'
