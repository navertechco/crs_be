# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agent(models.Model):
    agent_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agent'


class Client(models.Model):
    client_id = models.BigIntegerField(primary_key=True)
    name_contact = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    legal_client_type_id = models.BigIntegerField()
    client_type_id = models.BigIntegerField()
    dni = models.CharField(unique=True, max_length=32)
    is_owner = models.BooleanField()
    name_contact_2 = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=64)
    origin_id = models.CharField(max_length=-1)
    phone = models.CharField(unique=True, max_length=64)
    address = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'client'


class Supplier(models.Model):
    supplier_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    supplier_type_id = models.BigIntegerField()
    supplier_rule_id = models.BigIntegerField()
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_id = models.BigIntegerField(unique=True)
    legal_name = models.CharField(unique=True, max_length=32)
    city_id = models.BigIntegerField(blank=True, null=True)
    commercial_name = models.CharField(max_length=32)
    contact_name = models.CharField(max_length=32)
    website = models.CharField(max_length=32, blank=True, null=True)
    payment_type_id = models.BigIntegerField(blank=True, null=True)
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


class TravelExpert(models.Model):
    travel_expert_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_expert'


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    surname = models.CharField(max_length=16, blank=True, null=True)
    lastname = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(unique=True, max_length=16, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    identification = models.CharField(unique=True, max_length=16)
    state = models.BigIntegerField()
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=64, blank=True, null=True)
    confirmation = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'user'
