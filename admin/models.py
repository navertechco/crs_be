# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalog(models.Model):
    catalog_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
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
    order = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=-1)
    code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_detail'
        unique_together = (('order', 'catalog_id'),)


class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    contact_name = models.CharField(max_length=64)
    legal_client_type_id = models.BigIntegerField()
    client_type_id = models.BigIntegerField()
    client_dni = models.CharField(max_length=32)
    is_owner = models.BooleanField()
    contact_name_2 = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64)
    origin_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    description = models.CharField(max_length=-1)
    brith_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'client'


class Day(models.Model):
    day_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = models.BigIntegerField()
    transport = models.ForeignKey('Transport', models.DO_NOTHING)
    meals = models.TextField(blank=True, null=True)  # This field type is a guess.
    day_name = models.CharField(max_length=-1, blank=True, null=True)
    day_description = models.CharField(max_length=-1, blank=True, null=True)
    day_date = models.DateField(blank=True, null=True)
    day_observation = models.CharField(max_length=-1, blank=True, null=True)
    day_previous = models.CharField(max_length=-1, blank=True, null=True)
    day_next = models.CharField(max_length=-1, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day'


class Destination(models.Model):
    destination_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    port = models.BooleanField()
    destination_name = models.CharField(max_length=-1)
    destination_title = models.CharField(max_length=-1)
    hotel_id = models.IntegerField()
    airport_id = models.IntegerField()
    has_airport = models.BooleanField()
    description = models.CharField(max_length=-1, blank=True, null=True)
    previous = models.CharField(max_length=-1, blank=True, null=True)
    next = models.CharField(max_length=-1, blank=True, null=True)
    destination_option_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'destination'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Experience(models.Model):
    experience_id = models.IntegerField(primary_key=True)
    destination = models.ForeignKey(Destination, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = models.BigIntegerField()
    service_type_id = models.BigIntegerField()
    budget_id = models.BigIntegerField()
    delimiter_id = models.BigIntegerField()
    travel_ritm_id = models.BigIntegerField()
    experience_title = models.CharField(max_length=-1, blank=True, null=True)
    experience_photo = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    experience_previous = models.CharField(max_length=-1, blank=True, null=True)
    experience_next = models.CharField(max_length=-1, blank=True, null=True)
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
    option_id = models.IntegerField()
    is_included = models.BooleanField()
    description = models.CharField(max_length=-1, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'included_option'
        unique_together = (('tour_id', 'option_id'),)


class NetRate(models.Model):
    net_rate_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    final_detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    tour_id = models.IntegerField()
    description = models.CharField(max_length=-1, blank=True, null=True)

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
    age_friendly_range_id = models.BigIntegerField()
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
    supplier_type_id = models.BigIntegerField()
    supplier_rule_id = models.BigIntegerField()
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_id = models.BigIntegerField()
    legal_name = models.CharField(max_length=32)
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
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class Tour(models.Model):
    tour_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    title = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.CharField(max_length=-1, blank=True, null=True)
    valid = models.DateField(blank=True, null=True)
    destination_country_id = models.IntegerField(blank=True, null=True)
    purpose_id = models.IntegerField(blank=True, null=True)
    accomodation_type_id = models.IntegerField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    contact_agent = models.CharField(max_length=-1, blank=True, null=True)
    pasengers = models.IntegerField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    nights = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    cover_title = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class TourDetail(models.Model):
    tour_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    itinerary_state_id = models.IntegerField()
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
    transport_range_id = models.BigIntegerField()
    transport_service_id = models.BigIntegerField()
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
    state = models.BigIntegerField()
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=64, blank=True, null=True)
    confirmation = models.CharField(max_length=-1)
    user_type_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
