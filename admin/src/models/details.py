# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ItineraryDay(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    itinerary_day_id = models.BigIntegerField()
    promo_id = models.BigIntegerField()
    service_id = models.BigIntegerField()
    amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'itinerary_day'


class ServiceCruise(models.Model):
    internet = models.BooleanField()
    tc_cons = models.BooleanField()
    wetsuits = models.BooleanField()
    dr_name = models.CharField(max_length=32)
    description = models.CharField(max_length=32, blank=True, null=True)
    fleet = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator_name = models.CharField(max_length=32, blank=True, null=True)
    owner_name = models.CharField(max_length=32, blank=True, null=True)
    ship_name = models.CharField(max_length=-1)
    aet = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    pax_daily_rate = models.FloatField(blank=True, null=True)
    cab_number = models.BigIntegerField(blank=True, null=True)
    cab_type = models.BigIntegerField(blank=True, null=True)
    category = models.BigIntegerField(blank=True, null=True)
    format = models.BigIntegerField(blank=True, null=True)
    modality = models.BigIntegerField(blank=True, null=True)
    pax = models.BigIntegerField(blank=True, null=True)
    port_registry = models.BigIntegerField(blank=True, null=True)
    ship_type = models.BigIntegerField(blank=True, null=True)
    tri_number = models.BigIntegerField(blank=True, null=True)
    additionals = models.TextField(blank=True, null=True)  # This field type is a guess.
    constraints = models.TextField(blank=True, null=True)  # This field type is a guess.
    guides = models.TextField(blank=True, null=True)  # This field type is a guess.
    itinerary = models.TextField(blank=True, null=True)  # This field type is a guess.
    web_page = models.CharField(max_length=-1, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    id = models.BigIntegerField(primary_key=True)
    service_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'service_cruise'


class ServiceHotel(models.Model):
    num_room_types = models.IntegerField(blank=True, null=True)
    balcony = models.BooleanField(blank=True, null=True)
    budget_fk = models.BigIntegerField(blank=True, null=True)
    child_friendly = models.BooleanField(blank=True, null=True)
    extra_bed = models.BooleanField(blank=True, null=True)
    fit_rate = models.BooleanField(blank=True, null=True)
    group_from = models.BigIntegerField(blank=True, null=True)
    group_rate = models.BigIntegerField(blank=True, null=True)
    guide_transport = models.FloatField(blank=True, null=True)
    hotel_name = models.CharField(max_length=-1, blank=True, null=True)
    infant_friendly = models.BooleanField(blank=True, null=True)
    key_activity_type_fk = models.BigIntegerField(blank=True, null=True)
    max_capacity = models.BigIntegerField(blank=True, null=True)
    midweek_rate = models.FloatField(blank=True, null=True)
    observations = models.CharField(max_length=-1, blank=True, null=True)
    outside_window = models.BooleanField(blank=True, null=True)
    pet_friendly = models.BooleanField(blank=True, null=True)
    purpouse_fk = models.BigIntegerField(blank=True, null=True)
    roh_from = models.BooleanField(blank=True, null=True)
    ro_house = models.BooleanField(blank=True, null=True)
    romantic_package = models.TextField(blank=True, null=True)  # This field type is a guess.
    romantic_rate = models.FloatField(blank=True, null=True)
    room_category = models.CharField(max_length=-1, blank=True, null=True)
    room_description = models.CharField(max_length=-1, blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    supplier_fk = models.BigIntegerField(blank=True, null=True)
    tax1_iva = models.FloatField(blank=True, null=True)
    tax2_service = models.FloatField(blank=True, null=True)
    tax3_citytax = models.FloatField(blank=True, null=True)
    tax4 = models.FloatField(blank=True, null=True)
    terrace_patio = models.BooleanField(blank=True, null=True)
    tub_jacuzzi = models.BooleanField(blank=True, null=True)
    weekend_rate = models.FloatField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    id = models.BigIntegerField(primary_key=True)
    service_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'service_hotel'
