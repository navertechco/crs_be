# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .utils.catalogfield import CatalogField

class Catalog(models.Model):
    catalog_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'catalog'
    def dict(self):
        return {'catalog_id': self.catalog_id, "description":self.description}


class CatalogDetail(models.Model):
    catalog_detail_id = models.IntegerField(primary_key=True)
    catalog_id = models.BigIntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    order = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'catalog_detail'
        unique_together = (('order', 'catalog_id'),)
    def dict(self):
        return {'catalog_detail_id': self.catalog_detail_id, "catalog_id":self.catalog_id, "order":self.order, "description":self.description}

        
# tt = CatalogField("key_activity", Catalog, CatalogDetail)

class Day(models.Model):
    day_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = CatalogField("key_activity", Catalog, CatalogDetail)
    included_option = models.ForeignKey('IncludedOption', models.DO_NOTHING)
    transport = models.ForeignKey('Transport', models.DO_NOTHING)
    meals = models.TextField(blank=True, null=True)  # This field type is a guess.
    day_name = models.CharField(max_length=100, blank=True, null=True)
    day_description = models.CharField(max_length=100, blank=True, null=True)
    day_date = models.DateField(blank=True, null=True)
    day_observation = models.CharField(max_length=100, blank=True, null=True)
    day_previous = models.CharField(max_length=100, blank=True, null=True)
    day_next = models.CharField(max_length=100, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day'


class Destination(models.Model):
    destination_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    port = models.BooleanField()
    destination_name = models.CharField(max_length=100)
    destination_title = models.CharField(max_length=100)
    hotel_id = CatalogField("hotel", Catalog, CatalogDetail)
    airport_id = CatalogField("airport", Catalog, CatalogDetail)
    has_airport = models.BooleanField()
    description = models.CharField(max_length=100, blank=True, null=True)
    previous = models.CharField(max_length=100, blank=True, null=True)
    next = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destination'


class Experience(models.Model):
    experience_id = models.IntegerField(primary_key=True)
    destination = models.ForeignKey(Destination, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = CatalogField("key_activity", Catalog, CatalogDetail)
    service_type_id = CatalogField("service_type", Catalog, CatalogDetail)
    budget_id = CatalogField("budget", Catalog, CatalogDetail)
    delimiter_id = CatalogField("delimiter", Catalog, CatalogDetail)
    travel_ritm_id = CatalogField("travel_rhythm", Catalog, CatalogDetail)
    experience_title = models.CharField(max_length=100, blank=True, null=True)
    experience_photo = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    experience_previous = models.CharField(max_length=100, blank=True, null=True)
    experience_next = models.CharField(max_length=100, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'experience'


class ExperienceDetail(models.Model):
    experience_detail_id = models.IntegerField(primary_key=True)
    service_id = models.IntegerField()
    experience_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'experience_detail'
        unique_together = (('service_id', 'experience_id'),)


class IncludedOption(models.Model):
    included_option_id = models.IntegerField(primary_key=True)
    tour_id = models.IntegerField()
    option = CatalogField("included_option", Catalog, CatalogDetail)
    is_included = models.BooleanField()
    description = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'included_option'
        # unique_together = (('tour_id', 'option_id'),)


class NetRate(models.Model):
    net_rate_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    final_detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    tour_id = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'net_rate'


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
    age_friendly_range_id = CatalogField("age_friendly_range", Catalog, CatalogDetail)
    child_frendly = models.BooleanField()
    infant_friendly = models.BooleanField()
    observation = models.CharField(max_length=64, blank=True, null=True)
    max_capacity = models.BigIntegerField()
    pet_friendly = models.BooleanField()
    props = models.TextField()  # This field type is a guess.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service'


class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    supplier_type_id = CatalogField("supplier_type", Catalog, CatalogDetail)
    supplier_rule_id = CatalogField("supplier_rule", Catalog, CatalogDetail)
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_id = models.BigIntegerField()
    legal_name = models.CharField(max_length=32)
    city_id = CatalogField("city", Catalog, CatalogDetail)
    commercial_name = models.CharField(max_length=32)
    contact_name = models.CharField(max_length=32)
    website = models.CharField(max_length=32, blank=True, null=True)
    payment_type_id = CatalogField("payment_type", Catalog, CatalogDetail)
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
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class TourDetail(models.Model):
    tour_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    itinerary_state_id = CatalogField("itinerary_state", Catalog, CatalogDetail)
    destination_id = models.IntegerField()
    day_id = models.IntegerField()
    experience_id = models.IntegerField()
    tour_detail_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tour_detail'
        unique_together = (('tour_id', 'destination_id', 'day_id', 'experience_id'),)


class Transport(models.Model):
    transport_id = models.BigIntegerField(primary_key=True)
    transport_range_id = CatalogField("transport_range", Catalog, CatalogDetail)
    transport_service_id = CatalogField("transport_service", Catalog, CatalogDetail)
    rate = models.FloatField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transport'
        # unique_together = (('transport_range_id', 'transport_service_id'),)


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    firstname = models.CharField(max_length=16, blank=True, null=True)
    lastname = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(unique=True, max_length=16, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    identification = models.CharField(unique=True, max_length=16)
    state = models.BigIntegerField()
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=64, blank=True, null=True)
    confirmation = models.CharField(max_length=100)
    user_type_id = CatalogField("user_type", Catalog, CatalogDetail)

    class Meta:
        managed = False
        db_table = 'user'
