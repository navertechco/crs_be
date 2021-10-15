# Generated by Django 3.2.7 on 2021-10-15 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id_budget', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'budget',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id_catalogue', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'catalogue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CatalogueDetail',
            fields=[
                ('id_catalogue_detail', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'catalogue_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('dni', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id_client_type', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'client_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delimiter',
            fields=[
                ('id_delimiter', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'delimiter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id_destination', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'destination',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DestinationService',
            fields=[
                ('id_destination_service', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'destination_service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeyActivity',
            fields=[
                ('id_key_activity', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'key_activity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LegalClientType',
            fields=[
                ('id_legal_client_type', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'legal_client_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id_media', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'media',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id_media_type', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'media_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id_playlist', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'playlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistState',
            fields=[
                ('id_playlist_state', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'playlist_state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id_promo', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'promo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PromoDetail',
            fields=[
                ('id_promo_detail', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'promo_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purpouse',
            fields=[
                ('id_purpouse', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'purpouse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id_quote', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('id_travelexper_user', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'quote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuoteDetail',
            fields=[
                ('id_quote_detail', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'quote_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuoteState',
            fields=[
                ('id_quote_state', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'quote_state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id_service', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id_service_detail', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'service_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'service_supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id_service_type', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'service_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id_supplier', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SupplierType',
            fields=[
                ('id_supplier_type', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'supplier_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TravelRitm',
            fields=[
                ('id_travel_ritm', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'travel_ritm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('props', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
