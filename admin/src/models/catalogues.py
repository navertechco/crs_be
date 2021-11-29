# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgeFriendlyRange(models.Model):
    age_friendly_range_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'age_friendly_range'


class Budget(models.Model):
    budget_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'budget'


class City(models.Model):
    city_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city'


class ClientType(models.Model):
    client_type_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_type'


class CountryDestination(models.Model):
    country_destination_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'country_destination'


class Delimiter(models.Model):
    delimiter_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delimiter'


class Destination(models.Model):
    destination_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'destination'


class IncludedOption(models.Model):
    included_option_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'included_option'


class ItineraryState(models.Model):
    itinerary_state_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'itinerary_state'


class KeyActivity(models.Model):
    key_activity_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'key_activity'


class LegalClientType(models.Model):
    legal_client_type_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'legal_client_type'


class MediaType(models.Model):
    media_type_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media_type'


class Origin(models.Model):
    origin_id = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'origin'


class PaymentType(models.Model):
    payment_type_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment_type'


class Purpose(models.Model):
    purpose_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purpose'


class ServiceType(models.Model):
    service_type_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_type'


class SupplierRule(models.Model):
    supplier_rule_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supplier_rule'


class SupplierType(models.Model):
    supplier_type_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supplier_type'


class TransportRange(models.Model):
    transport_range_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=128)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transport_range'


class TransportService(models.Model):
    transport_service_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=128)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transport_service'


class TravelRitm(models.Model):
    travel_ritm_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    capacity = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'travel_ritm'
