# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Catalog(models.Model):
    catalog_id = models.BigIntegerField(primary_key=True)
    catalog_name = models.CharField(max_length=-1, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'catalog'


class CatalogDetail(models.Model):
    catalog_detail_id = models.IntegerField(primary_key=True)
    catalog_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'catalog_detail'

def findCatalog(name):
    return CatalogDetail.objects.filter(catalog_id=Catalog.objects.filter(catalog_name=name).first())

class Day(models.Model):
    day_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = findCatalog("key_activity")
    included_option_id = findCatalog("included_option")
    transport = models.ForeignKey('Transport', models.DO_NOTHING)
    meals = models.TextField(blank=True, null=True)  # This field type is a guess.
    day_name = models.CharField(max_length=-1, blank=True, null=True)
    day_description = models.CharField(max_length=-1, blank=True, null=True)
    day_date = models.DateField(blank=True, null=True)
    day_observation = models.CharField(max_length=-1, blank=True, null=True)
    day_previous = models.CharField(max_length=-1, blank=True, null=True)
    day_next = models.CharField(max_length=-1, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    itinerary_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day'


class DayDetail(models.Model):
    day_detail_id = models.IntegerField(primary_key=True)
    day_id = models.IntegerField()
    experience_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'day_detail'


class Destination(models.Model):
    destination_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    port = models.BooleanField()
    destination_name = models.CharField(max_length=-1)
    destination_title = models.CharField(max_length=-1)
    hotel_id = models.IntegerField()
    airport_id = models.IntegerField(blank=True, null=True)
    has_airport = models.BooleanField()
    description = models.CharField(max_length=-1, blank=True, null=True)
    previous = models.CharField(max_length=-1, blank=True, null=True)
    next = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destination'


class EndService(models.Model):
    end_service_id = models.IntegerField(primary_key=True)
    net_rate = models.ForeignKey('NetRate', models.DO_NOTHING)
    included = models.TextField(blank=True, null=True)  # This field type is a guess.
    not_included = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'end_service'


class Experience(models.Model):
    experience_id = models.IntegerField(primary_key=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
    destination = models.ForeignKey(Destination, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = findCatalog("key_activity")
    service_type_id = findCatalog("service_type")
    budget_id = findCatalog("budget")
    delimiter_id = findCatalog("delimiter")
    travel_ritm_id = findCatalog("travel_ritm")
    experience_title = models.CharField(max_length=-1, blank=True, null=True)
    experience_photo = models.CharField(max_length=-1, blank=True, null=True)
    experience_description = models.CharField(max_length=-1, blank=True, null=True)
    experience_previous = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experience'


class NetRate(models.Model):
    net_rate_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    final_detail = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'net_rate'


class NetRateDetail(models.Model):
    net_rate_detail_id = models.IntegerField(primary_key=True)
    net_rate_id = models.IntegerField()
    itinerary_id = models.IntegerField()
    service_experience_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'net_rate_detail'


class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    me = models.BooleanField()
    open_days = models.CharField(max_length=16)
    close_time = models.TimeField()
    open_time = models.TimeField()
    cost = models.FloatField()
    selling_price = models.FloatField()
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    duration = models.BigIntegerField()
    age_friendly_range_id = findCatalog("age_friendly_range")
    child_frendly = models.BooleanField()
    infant_friendly = models.BooleanField()
    observation = models.CharField(max_length=64, blank=True, null=True)
    max_capacity = models.BigIntegerField()
    pet_friendly = models.BooleanField()
    props = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'service'


class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    supplier_type_id = findCatalog("supplier_type")
    supplier_rule_id = findCatalog("supplier_rule")
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_id = models.BigIntegerField(blank=True, null=True)
    legal_name = models.CharField(max_length=32)
    city_id = findCatalog("city")
    commercial_name = models.CharField(max_length=32)
    contact_name = models.CharField(max_length=32)
    website = models.CharField(max_length=32, blank=True, null=True)
    payment_type_id = findCatalog("payment_type")
    credit_days = models.CharField(max_length=32, blank=True, null=True)
    finance_email = models.CharField(max_length=32, blank=True, null=True)
    commercial_email = models.CharField(max_length=32, blank=True, null=True)
    finance_phone = models.BigIntegerField(blank=True, null=True)
    commercial_phone = models.BigIntegerField(blank=True, null=True)
    sector = models.CharField(max_length=32, blank=True, null=True)
    principal_street = models.CharField(max_length=32, blank=True, null=True)
    secondary_street = models.CharField(max_length=32, blank=True, null=True)
    building_number = models.CharField(max_length=32, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class Transport(models.Model):
    transport_id = models.BigIntegerField(primary_key=True)
    transport_range_id = findCatalog("transport_range")
    transport_service_id = findCatalog("transport_service")
    rate = models.FloatField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transport'
        unique_together = (('transport_range_id', 'transport_service_id'),)


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    firstname = models.CharField(max_length=16, blank=True, null=True)
    lastname = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(unique=True, max_length=16, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    identification = models.CharField(unique=True, max_length=16)
    state = findCatalog("user_state")
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=64, blank=True, null=True)
    confirmation = models.CharField(max_length=-1)
    user_type_id = findCatalog("user_type")

    class Meta:
        managed = False
        db_table = 'user'
