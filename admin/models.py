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


class Agent(models.Model):
    agent_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agent'


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


class IncludedOption(models.Model):
    included_option_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'included_option'


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
    playlist_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary'
        unique_together = (('pax', 'agent_id', 'client_id', 'itinerary_state_id', 'country_destination_id', 'budget_id', 'purpose_id'),)


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


class Media(models.Model):
    media_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    media_type_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'media'


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


class Purpose(models.Model):
    purpose_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purpose'


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


class ServiceType(models.Model):
    service_type_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_type'


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


class TravelExpert(models.Model):
    travel_expert_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_expert'


class TravelRitm(models.Model):
    travel_ritm_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    capacity = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'travel_ritm'


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
