# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ItineraryDay(models.Model):
    itinerary_day_id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    itinerary_id = models.BigIntegerField()
    day_id = models.BigIntegerField()
    travel_ritm_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'itinerary_day'


class PlaylistMedia(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    playlist_id = models.BigIntegerField()
    media_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'playlist_media'
