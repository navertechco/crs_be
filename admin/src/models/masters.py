# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Day(models.Model):
    day_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = models.BigIntegerField()
    included_option_id = models.BigIntegerField()
    destination_id = models.BigIntegerField()
    transport = models.ForeignKey('Transport', models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day'


class Itinerary(models.Model):
    itinerary_id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    pax = models.IntegerField()
    agent_id = models.BigIntegerField(blank=True, null=True)
    travel_expert_id = models.BigIntegerField(blank=True, null=True)
    client_id = models.BigIntegerField()
    itinerary_state_id = models.BigIntegerField()
    country_destination_id = models.BigIntegerField()
    budget_id = models.BigIntegerField()
    purpose_id = models.BigIntegerField()
    reproductions = models.BigIntegerField()
    match = models.TextField(blank=True, null=True)  # This field type is a guess.
    day_destinations = models.TextField(blank=True, null=True)  # This field type is a guess.
    arrival_date = models.DateField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    days_duration = models.BigIntegerField(blank=True, null=True)
    hours_duration = models.BigIntegerField(blank=True, null=True)
    playlist = models.ForeignKey('Playlist', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary'
        unique_together = (('pax', 'agent_id', 'client_id', 'itinerary_state_id', 'country_destination_id', 'budget_id', 'purpose_id'),)


class Media(models.Model):
    media_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    media_type_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'media'


class Playlist(models.Model):
    playlist_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    playlist = models.TextField(blank=True, null=True)  # This field type is a guess.
    playlist_slug = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'playlist'


class Promo(models.Model):
    promo_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promo'


class Service(models.Model):
    service_id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    destination_id = models.BigIntegerField()
    supplier_id = models.BigIntegerField()
    key_activity_id = models.BigIntegerField()
    service_type_id = models.BigIntegerField()
    budget_id = models.BigIntegerField()
    delimiter_id = models.BigIntegerField()
    me = models.BooleanField()
    open_days = models.CharField(max_length=16)
    close_time = models.TimeField()
    open_time = models.TimeField()
    cost = models.FloatField()
    selling_price = models.FloatField()
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    duration = models.BigIntegerField()
    age_friendly_range_id = models.BigIntegerField()
    child_frendly = models.BooleanField()
    infant_friendly = models.BooleanField()
    observation = models.CharField(max_length=64, blank=True, null=True)
    max_capacity = models.BigIntegerField()
    pet_friendly = models.BooleanField()
    props = models.TextField()  # This field type is a guess.
    travel_ritm_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'service'


class Transport(models.Model):
    transport_id = models.BigIntegerField(primary_key=True)
    transport_range_id = models.BigIntegerField()
    transport_service_id = models.BigIntegerField()
    rate = models.FloatField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transport'
