# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    id_activity = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_media_fk = models.ForeignKey('Media', models.DO_NOTHING, db_column='id_media_fk')
    activity_type_fk = models.ForeignKey('CatalogueDetail', models.DO_NOTHING, db_column='activity_type_fk')
    id_schedule_fk = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='id_schedule_fk')

    class Meta:
        managed = False
        db_table = 'activity'


class Budget(models.Model):
    id_budget = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'budget'


class Catalogue(models.Model):
    id_catalogue = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'catalogue'


class CatalogueDetail(models.Model):
    id_catalogue_fk = models.ForeignKey(Catalogue, models.DO_NOTHING, db_column='id_catalogue_fk')
    order = models.BigIntegerField()
    description = models.CharField(max_length=64)
    id_catalogue_detail = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'catalogue_detail'


class Contact(models.Model):
    id_contact = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    contact_state_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='contact_state_fk')
    contact_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='contact_type_fk')

    class Meta:
        managed = False
        db_table = 'contact'


class Destiny(models.Model):
    id_destiny = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_media_fk = models.ForeignKey('Media', models.DO_NOTHING, db_column='id_media_fk')
    id_schedule_fk = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='id_schedule_fk')

    class Meta:
        managed = False
        db_table = 'destiny'


class Experience(models.Model):
    id_experience = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'experience'


class ExperienceDetail(models.Model):
    id_experience_detail = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_destiny_fk = models.ForeignKey(Destiny, models.DO_NOTHING, db_column='id_destiny_fk')
    id_activity_fk = models.ForeignKey(Activity, models.DO_NOTHING, db_column='id_activity_fk')
    id_experience_fk = models.ForeignKey(Experience, models.DO_NOTHING, db_column='id_experience_fk')
    id_schedule_fk = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='id_schedule_fk')

    class Meta:
        managed = False
        db_table = 'experience_detail'


class Media(models.Model):
    id_media = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'media'


class Opportunity(models.Model):
    id_opportunity = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_salesman_fk = models.ForeignKey('User', models.DO_NOTHING, db_column='id_salesman_fk')
    id_contact_fk = models.ForeignKey(Contact, models.DO_NOTHING, db_column='id_contact_fk')
    id_quote_fk = models.ForeignKey('Quote', models.DO_NOTHING, db_column='id_quote_fk')
    id_budget_fk = models.ForeignKey(Budget, models.DO_NOTHING, db_column='id_budget_fk')
    status_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='status_type_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opportunity'


class Problem(models.Model):
    id_problem = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_experience = models.ForeignKey(Experience, models.DO_NOTHING, db_column='id_experience')

    class Meta:
        managed = False
        db_table = 'problem'


class ProblemDetail(models.Model):
    id_problem_detail = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_problem_fk = models.ForeignKey(Problem, models.DO_NOTHING, db_column='id_problem_fk')
    problem_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='problem_type_fk')
    is_compensable = models.BooleanField()
    compensation_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='compensation_type_fk')
    compensation_amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'problem_detail'


class Product(models.Model):
    id_product = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_supplier_fk = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='id_supplier_fk')

    class Meta:
        managed = False
        db_table = 'product'


class Promo(models.Model):
    id_promo = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'promo'


class PromoDetail(models.Model):
    id_promo_detail = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_promo_fk = models.ForeignKey(Promo, models.DO_NOTHING, db_column='id_promo_fk')
    id_product_fk = models.ForeignKey(Product, models.DO_NOTHING, db_column='id_product_fk', blank=True, null=True)
    id_service_fk = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_service_fk', blank=True, null=True)
    discount = models.BigIntegerField()
    promo_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='promo_type_fk')
    id_experience_fk = models.ForeignKey(Experience, models.DO_NOTHING, db_column='id_experience_fk')

    class Meta:
        managed = False
        db_table = 'promo_detail'


class Quote(models.Model):
    id_quote = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    quote_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='quote_type_fk')

    class Meta:
        managed = False
        db_table = 'quote'


class QuoteDetail(models.Model):
    id_quote_detail = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_quote_fk = models.ForeignKey(Quote, models.DO_NOTHING, db_column='id_quote_fk')
    id_experience_fk = models.ForeignKey(Experience, models.DO_NOTHING, db_column='id_experience_fk')

    class Meta:
        managed = False
        db_table = 'quote_detail'


class Schedule(models.Model):
    id_schedule = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Service(models.Model):
    id_service = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_supplier_fk = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='id_supplier_fk')

    class Meta:
        managed = False
        db_table = 'service'


class Supplier(models.Model):
    id_supplier = models.BigIntegerField(primary_key=True)
    props = models.TextField()  # This field type is a guess.
    id_supplier_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='id_supplier_type_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class User(models.Model):
    id_user = models.CharField(primary_key=True, max_length=15)
    props = models.TextField()  # This field type is a guess.
    id_user_type_fk = models.ForeignKey(CatalogueDetail, models.DO_NOTHING, db_column='id_user_type_fk')

    class Meta:
        managed = False
        db_table = 'user'
