# Generated by Django 3.1.13 on 2021-10-18 15:05

from django.db import migrations, models
import django.db.models.deletion
import pantalla.models


class Migration(migrations.Migration):

    dependencies = [
        ('pantalla', '0002_client_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='promodetail',
            name='discount',
            field=models.FloatField(default=0, max_length=8, validators=[pantalla.models.validate_decimals]),
        ),
        migrations.AddField(
            model_name='quote',
            name='pax',
            field=models.IntegerField(default=1, max_length=4),
        ),
        migrations.AddField(
            model_name='quotedetail',
            name='amount',
            field=models.FloatField(default=0, max_length=8, validators=[pantalla.models.validate_decimals]),
        ),
        migrations.AlterField(
            model_name='quote',
            name='id_quote_state',
            field=models.ForeignKey(db_column='id_quote_state', default=1, on_delete=django.db.models.deletion.CASCADE, to='pantalla.quotestate'),
        ),
    ]