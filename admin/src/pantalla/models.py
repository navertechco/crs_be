# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .utils.catalogfield import CatalogField, MasterCatalogField
class Catalog(models.Model):
    catalog_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'catalog'
    def __str__(self):
        return self.description
class CatalogDetail(models.Model):
    catalog_detail_id = models.AutoField(primary_key=True)
    catalog_id = models.IntegerField(choices=MasterCatalogField(Catalog))
    # catalog = models.ForeignKey('Catalog', models.DO_NOTHING)
    order = models.IntegerField(null=True)
    description = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    code = models.IntegerField()
    is_active = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'catalog_detail'
        unique_together = (('order', 'catalog_id', 'code',),('description',),)
        
    def __str__(self):
        return self.description
        
    @property
    def catalog(self):
        print(self)
        return models.BigIntegerField(choices=Catalog.objects.values_list('catalog_id', 'description').filter(catalog_id=self.catalog_id))
    def __str__(self):
        return str(Catalog.objects.values_list('catalog_id', 'description').filter(catalog_id=self.catalog_id)[0][1])+"->"+self.description+"->"+str(self.code)+"->"+str(self.is_active)
    def to_list(self):
        details = list(self.objects.values_list())
        return details
    # def __init__(self,  *args, **kwargs):
    #     super(CatalogDetail, self).__init__(*args, **kwargs)
    #     self.catalog_id = [o.catalog_id for o in list(
    #         Catalog.objects.filter(catalog_id=self.catalog_detail_id))][0]
class Day(models.Model):
    day_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    key_activity = models.IntegerField(db_column="key_activity_id", choices=CatalogField(
        "key_activity", Catalog, CatalogDetail))
    transport = models.ForeignKey('Transport', models.DO_NOTHING)
    day_name = models.CharField(max_length=100,  null=True)
    description = models.CharField(max_length=100) 
    day_previous = models.CharField(max_length=100,  null=True)
    day_observation = models.CharField(max_length=100, blank=True, null=True)
    day_next = models.CharField(max_length=100, blank=True, null=True) 
    meals = models.CharField(max_length=100, blank=True, null=True)
    tour_detail = models.ForeignKey('TourDetail', models.DO_NOTHING)

        
    class Meta:
        managed = False
        db_table = 'day'
    def __str__(self):
        return str(self.tour_detail)+"->"+self.description
    
    
class DayDetail(models.Model):
    day_detail_id = models.AutoField(primary_key=True)
    service = models.ForeignKey('Service', models.DO_NOTHING)
    experience = models.ForeignKey('Experience', models.DO_NOTHING)
    day = models.ForeignKey("Day", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'day_detail'
        unique_together = (('day', 'experience', 'service'),)
    
    def __str__(self):
        return str(self.day)+"->"+str(self.experience)+"->"+str(self.service)
    
class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    port = models.BooleanField()
    destination_name = models.CharField(max_length=100)
    destination_title = models.CharField(max_length=100)
    hotel_id = models.IntegerField(
        choices=CatalogField("hotel", Catalog, CatalogDetail))
    airport_id = models.IntegerField(
        choices=CatalogField("airport", Catalog, CatalogDetail))
    has_airport = models.BooleanField()
    description = models.CharField(max_length=100)
    previous = models.CharField(max_length=100,  null=True)
    next = models.CharField(max_length=100, blank=True,  null=True)
    class Meta:
        managed = False
        db_table = 'destination'
    def __str__(self):
        return self.description
class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
    destination = models.ForeignKey("Destination", models.DO_NOTHING)
    destination_option = models.IntegerField(db_column="destination_option_id",
        choices=CatalogField("destination_option", Catalog, CatalogDetail))
    key_activity = models.IntegerField(db_column="key_activity_id",
                                       choices=CatalogField("key_activity", Catalog, CatalogDetail))
    key_activity2 = models.IntegerField(db_column="key_activity2_id",
                                       choices=CatalogField("key_activity", Catalog, CatalogDetail))
    budget = models.IntegerField(db_column="budget_id",
                                 choices=CatalogField("budget", Catalog, CatalogDetail))
    delimiter = models.IntegerField(db_column="delimiter_id",
                                    choices=CatalogField("delimiter", Catalog, CatalogDetail))
    travel_ritm = models.IntegerField(db_column="travel_ritm_id",
                                      choices=CatalogField("travel_ritm", Catalog, CatalogDetail))
    experience_title = models.CharField(max_length=100,  null=True)
    experience_photo = models.CharField(max_length=100,  null=True)
    description = models.CharField(max_length=100)
    experience_previous = models.CharField(
        max_length=100,  null=True)
    experience_next = models.CharField(max_length=100,  null=True)
    detail = models.TextField( null=True, default = "GFG is best")
    class Meta:
        managed = False
        db_table = 'experience'
    def __str__(self):
        return "Destination: "+str(self.destination)+"-> Experience: "+self.description

class IncludedOption(models.Model):
    included_option_id = models.AutoField(primary_key=True)
    tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column="tour_id")
    option_id = models.IntegerField(
        choices=CatalogField("option", Catalog, CatalogDetail))
    is_included = models.BooleanField()
    description = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'included_option'
    def __str__(self):
        return str(self.tour)+"->"+str(self.description)+"->"+str(self.is_included)
        # unique_together = (('tour_id', 'option_id'),)
class NetRate(models.Model):
    net_rate_id = models.AutoField(primary_key=True)
    tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column="tour_id")
    description = models.CharField(max_length=100)
    has_approbed = models.BooleanField()
    # final_detail = models.TextField(default = '{"props":""}')
    class Meta:
        managed = False
        db_table = 'net_rate'
    def __str__(self):
        return str(self.tour)+"->"+str(self.description)+"->"+str(self.has_approbed)
class Service(models.Model):
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
    service_id = models.AutoField(primary_key=True)
    open_days = models.CharField(max_length=16)
    close_time = models.TimeField()
    open_time = models.TimeField()
    cost = models.FloatField()
    selling_price = models.FloatField()
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=100)
    duration = models.BigIntegerField()
    max_capacity = models.BigIntegerField()
    age_friendly_range_id = models.IntegerField(
        choices=CatalogField("age_friendly_range", Catalog, CatalogDetail))
    observation = models.CharField(max_length=64,  null=True)
    me = models.BooleanField()
    child_frendly = models.BooleanField()
    infant_friendly = models.BooleanField()
    pet_friendly = models.BooleanField()
    props = models.TextField(default='{"props":""}', null=True)
    destination = models.ForeignKey(
        'Destination', models.DO_NOTHING, db_column="destination_id",)
    class Meta:
        managed = False
        db_table = 'service'
    def __str__(self):
        return self.description
class Supplier(models.Model):
    description = models.CharField(max_length=100)
    supplier_id = models.AutoField(primary_key=True)
    supplier_type_id = models.IntegerField(
        choices=CatalogField("supplier_type", Catalog, CatalogDetail))
    supplier_rule_id = models.IntegerField(
        choices=CatalogField("supplier_rule", Catalog, CatalogDetail))
    tax_id = models.BigIntegerField()
    legal_name = models.CharField(max_length=32)
    city_id = models.IntegerField(
        choices=CatalogField("city", Catalog, CatalogDetail))
    commercial_name = models.CharField(max_length=32)
    contact_name = models.CharField(max_length=32)
    payment_type_id = models.IntegerField(
        choices=CatalogField("payment_type", Catalog, CatalogDetail))
    website = models.CharField(max_length=32,  blank=True, null=True)
    credit_days = models.CharField(max_length=32,  blank=True, null=True)
    finance_email = models.CharField(max_length=32,  blank=True, null=True)
    commercial_email = models.CharField(max_length=32,  blank=True, null=True)
    finance_phone = models.BigIntegerField(blank=True, null=True)
    commercial_phone = models.BigIntegerField(blank=True, null=True)
    sector = models.CharField(max_length=32,  blank=True, null=True)
    principal_street = models.CharField(max_length=32,  blank=True, null=True)
    secondary_street = models.CharField(max_length=32,  blank=True, null=True)
    building_number = models.CharField(max_length=32,  blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    # props = models.TextField( null=True)
    class Meta:
        managed = False
        db_table = 'supplier'
    def __str__(self):
        return self.description
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=64)
    legal_client_type_id = models.IntegerField(
        choices=CatalogField("legal_client_type", Catalog, CatalogDetail))
    client_type_id = models.IntegerField(
        choices=CatalogField("client_type", Catalog, CatalogDetail))
    client_dni = models.CharField(max_length=32)
    is_owner = models.BooleanField()
    contact_name_2 = models.CharField(max_length=64,  null=True)
    email = models.CharField(max_length=64)
    origin_id = models.IntegerField(
        choices=CatalogField("origin", Catalog, CatalogDetail))
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    description = models.CharField(max_length=100)
    brith_date = models.DateField()
    class Meta:
        managed = False
        db_table = 'client'
    def __str__(self):
        return self.description
class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    partner = models.CharField(max_length=100,  null=True)
    valid = models.DateField(null=True)
    destination_country_id = models.IntegerField(
        choices=CatalogField("destination_country", Catalog, CatalogDetail))
    purpose_id = models.IntegerField(
        choices=CatalogField("purpose", Catalog, CatalogDetail))
    accomodation_type_id = models.IntegerField(
        choices=CatalogField("budget", Catalog, CatalogDetail))
    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)
    contact_agent = models.ForeignKey('User', models.DO_NOTHING, db_column='contact_agent')
    pasengers = models.IntegerField(null=True)
    days = models.IntegerField(null=True)
    nights = models.IntegerField(null=True)
    description = models.CharField(max_length=100)
    # detail = models.TextField( null=True)
    cover_title = models.CharField(max_length=100,  null=True)
    class Meta:
        managed = False
        db_table = 'tour'
    def __str__(self):
        return str(self.client)+"-> Tour: "+self.description+"-> Days: "+str(self.days)+"-> Nights: "+str(self.nights)+"-> Pax: "+str(self.pasengers)
class TourDetail(models.Model):
    tour_detail_id = models.AutoField(primary_key=True) 
    destination = models.ForeignKey(
        'Destination', models.DO_NOTHING, db_column="destination_id",)
    tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column="tour_id",)
    class Meta:
        managed = False
        db_table = 'tour_detail'
        unique_together = (('tour', 'destination'),)
    def __str__(self):
        return str(self.tour)+"->"+str(self.destination)
        # unique_together = (('tour_id', 'destination_id',
        #                    'day_id', 'experience_id'),)
class Transport(models.Model):
    transport_id = models.BigAutoField(primary_key=True)
    transport_range_id = models.IntegerField(
        choices=CatalogField("transport_range", Catalog, CatalogDetail))
    transport_service_id = models.IntegerField(
        choices=CatalogField("transport_service", Catalog, CatalogDetail))
    rate = models.FloatField()
    description = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'transport'
    def __str__(self):
        return self.description
        # unique_together = (('transport_range_id', 'transport_service_id'),)
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)
    firstname = models.CharField(max_length=16,  null=True)
    lastname = models.CharField(max_length=16,  null=True)
    username = models.CharField(
        unique=True, max_length=16,  null=True)
    password = models.CharField(max_length=100,  null=True)
    identification = models.CharField(unique=True, max_length=16)
    state = models.BigIntegerField()
    email = models.CharField(max_length=64,  null=True)
    phone = models.CharField(unique=True, max_length=64,  null=True)
    user_type_id = models.IntegerField(
        choices=CatalogField("user_type", Catalog, CatalogDetail))
    is_active = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'user'
    def __str__(self):
        return self.description
