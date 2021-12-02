# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgeFriendlyRange(models.Model):
    age_friendly_range_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'age_friendly_range'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agent'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'budget'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'city'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Client(models.Model):
    description = models.CharField(max_length=64)
    client_id = models.AutoField(primary_key=True)
    name_contact = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    legal_client_type = models.ForeignKey('LegalClientType', models.DO_NOTHING)
    client_type = models.ForeignKey('ClientType', models.DO_NOTHING)
    origin = models.ForeignKey('Origin', models.DO_NOTHING)
    dni = models.CharField(unique=True, max_length=32)
    is_owner = models.BooleanField()
    name_contact_2 = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=64)
    phone = models.CharField(unique=True, max_length=64)
    address = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'client'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class ClientType(models.Model):
    client_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # This field type is a guess.
    props = models.TextField(blank=True, null=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'client_type'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class CountryDestination(models.Model):
    country_destination_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'country_destination'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Day(models.Model):
    day_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    key_activity = models.ForeignKey('KeyActivity', models.DO_NOTHING)
    included_option = models.ForeignKey('IncludedOption', models.DO_NOTHING)
    destination = models.ForeignKey('Destination', models.DO_NOTHING)
    transport = models.ForeignKey('Transport', models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Delimiter(models.Model):
    delimiter_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'delimiter'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'destination'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class IncludedOption(models.Model):
    included_option_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'included_option'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Itinerary(models.Model):
    itinerary_id = models.AutoField(primary_key=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.itinerary_id
    pax = models.IntegerField()
    agent = models.ForeignKey(
        'Agent', models.DO_NOTHING, blank=True, null=True)
    travel_expert = models.ForeignKey(
        'TravelExpert', models.DO_NOTHING, blank=True, null=True)
    # playlist = models.ForeignKey('Playlist', models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    itinerary_state = models.ForeignKey('ItineraryState', models.DO_NOTHING)
    country_destination = models.ForeignKey(
        'CountryDestination', models.DO_NOTHING)
    budget = models.ForeignKey('Budget', models.DO_NOTHING)
    purpose = models.ForeignKey('Purpose', models.DO_NOTHING)
    # reproductions = models.BigIntegerField()
    # match = models.TextField(blank=True, null=True)  # This field type is a guess.
    # day_destinations = models.TextField(blank=True, null=True)  # This field type is a guess.
    arrival_date = models.DateField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    # days_duration = models.BigIntegerField(blank=True, null=True)
    # hours_duration = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )
        unique_together = (('pax', 'agent', 'client', 'itinerary_state',
                           'country_destination', 'budget', 'purpose'),)


class ItineraryDay(models.Model):
    # created = models.DateTimeField()
    # updated = models.DateTimeField()
    def __str__(self):
        return self.description
    itinerary_day_id = models.AutoField(primary_key=True)
    promo = models.ForeignKey('Promo', models.DO_NOTHING)
    service = models.ForeignKey('Service', models.DO_NOTHING)
    amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'itinerary_day'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class ItineraryState(models.Model):
    itinerary_state_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'itinerary_state'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class KeyActivity(models.Model):
    key_activity_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'key_activity'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class LegalClientType(models.Model):
    legal_client_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'legal_client_type'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    media_type = models.ForeignKey('MediaType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'media'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class MediaType(models.Model):
    media_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'media_type'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Origin(models.Model):
    origin_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'origin'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'payment_type'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    # This field type is a guess.
    playlist = models.TextField(blank=True, null=True)
    playlist_slug = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'playlist'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Promo(models.Model):
    promo_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promo'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Purpose(models.Model):
    purpose_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'purpose'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    destination = models.ForeignKey(
        'Destination', models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey(
        'Supplier', models.DO_NOTHING, blank=True, null=True)
    key_activity = models.ForeignKey(
        'KeyActivity', models.DO_NOTHING, blank=True, null=True)
    service_type = models.ForeignKey(
        'ServiceType', models.DO_NOTHING, blank=True, null=True)
    budget = models.ForeignKey(
        'Budget', models.DO_NOTHING, blank=True, null=True)
    delimiter = models.ForeignKey(
        'Delimiter', models.DO_NOTHING, blank=True, null=True)
    age_friendly_range = models.ForeignKey(
        'AgeFriendlyRange', models.DO_NOTHING, blank=True, null=True)
    travel_ritm = models.ForeignKey(
        'TravelRitm', models.DO_NOTHING, blank=True, null=True)
    child_frendly = models.BooleanField()
    infant_friendly = models.BooleanField()
    me = models.BooleanField()
    pet_friendly = models.BooleanField()
    open_days = models.CharField(max_length=16)
    close_time = models.TimeField()
    open_time = models.TimeField()
    cost = models.FloatField()
    selling_price = models.FloatField()
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    duration = models.BigIntegerField()
    observation = models.CharField(max_length=64, blank=True, null=True)
    max_capacity = models.BigIntegerField()
    props = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'service'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class ServiceCruise(models.Model):
    internet = models.BooleanField()
    tc_cons = models.BooleanField()
    wetsuits = models.BooleanField()
    dr_name = models.CharField(max_length=32)
    description = models.CharField(max_length=32, blank=True, null=True)
    # This field type is a guess.
    fleet = models.TextField(blank=True, null=True)
    operator_name = models.CharField(max_length=32, blank=True, null=True)
    owner_name = models.CharField(max_length=32, blank=True, null=True)
    ship_name = models.CharField(max_length=64)
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
    # This field type is a guess.
    additionals = models.TextField(blank=True, null=True)
    # This field type is a guess.
    constraints = models.TextField(blank=True, null=True)
    # This field type is a guess.
    guides = models.TextField(blank=True, null=True)
    # This field type is a guess.
    itinerary = models.TextField(blank=True, null=True)
    web_page = models.CharField(max_length=64, blank=True, null=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(
        'Service', models.DO_NOTHING, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'service_cruise'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


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
    hotel_name = models.CharField(max_length=64, blank=True, null=True)
    infant_friendly = models.BooleanField(blank=True, null=True)
    key_activity_type_fk = models.BigIntegerField(blank=True, null=True)
    max_capacity = models.BigIntegerField(blank=True, null=True)
    midweek_rate = models.FloatField(blank=True, null=True)
    observations = models.CharField(max_length=64, blank=True, null=True)
    outside_window = models.BooleanField(blank=True, null=True)
    pet_friendly = models.BooleanField(blank=True, null=True)
    purpouse_fk = models.BigIntegerField(blank=True, null=True)
    roh_from = models.BooleanField(blank=True, null=True)
    ro_house = models.BooleanField(blank=True, null=True)
    # This field type is a guess.
    romantic_package = models.TextField(blank=True, null=True)
    romantic_rate = models.FloatField(blank=True, null=True)
    room_category = models.CharField(max_length=64, blank=True, null=True)
    room_description = models.CharField(max_length=64, blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    supplier_fk = models.BigIntegerField(blank=True, null=True)
    tax1_iva = models.FloatField(blank=True, null=True)
    tax2_service = models.FloatField(blank=True, null=True)
    tax3_citytax = models.FloatField(blank=True, null=True)
    tax4 = models.FloatField(blank=True, null=True)
    terrace_patio = models.BooleanField(blank=True, null=True)
    tub_jacuzzi = models.BooleanField(blank=True, null=True)
    weekend_rate = models.FloatField(blank=True, null=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(
        'Service', models.DO_NOTHING, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'service_hotel'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class ServiceType(models.Model):
    service_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'service_type'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    supplier_type = models.ForeignKey(
        'SupplierType', models.DO_NOTHING, blank=True, null=True)
    supplier_rule = models.ForeignKey(
        'SupplierRule', models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey(
        'PaymentType', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)
    tax_id = models.BigIntegerField(unique=True)
    legal_name = models.CharField(unique=True, max_length=32)
    commercial_name = models.CharField(max_length=32)
    contact_name = models.CharField(max_length=32)
    website = models.CharField(max_length=32, blank=True, null=True)
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
    # This field type is a guess.
    props = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class SupplierRule(models.Model):
    supplier_rule_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'supplier_rule'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class SupplierType(models.Model):
    supplier_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'supplier_type'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class Transport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    transport_range = models.ForeignKey('TransportRange', models.DO_NOTHING)
    transport_service = models.ForeignKey(
        'TransportService', models.DO_NOTHING)
    description = models.CharField(max_length=64)
    rate = models.FloatField()
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'transport'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class TransportRange(models.Model):
    transport_range_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=128)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'transport_range'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class TransportService(models.Model):
    transport_service_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=128)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'transport_service'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class TravelExpert(models.Model):
    travel_expert_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_expert'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class TravelRitm(models.Model):
    travel_ritm_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    capacity = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'travel_ritm'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    def __str__(self):
        return self.description
    firstname = models.CharField(max_length=16, blank=True, null=True)
    lastname = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(
        unique=True, max_length=16, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    identification = models.CharField(unique=True, max_length=16)
    # state = models.BigIntegerField()
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=64, blank=True, null=True)
    # confirmation = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user'
        permissions = (
            ('add_item', 'Can add item'),
            ('change_item', 'Can change item'),
            ('delete_item', 'Can delete item'),
        )
