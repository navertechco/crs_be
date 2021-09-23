# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)
    answer_text = models.CharField(max_length=128)
    is_correct = models.BooleanField()
    id_question_fk = models.ForeignKey('Question', models.CASCADE, db_column='id_question_fk')

    class Meta:
        managed = False
        db_table = 'answer'
    def __str__(self):
        return str(self.answer_text)

class DetailCatalogue(models.Model):
    id_master_catalogue_fk = models.ForeignKey('MasterCatalogue', models.CASCADE, db_column='id_master_catalogue_fk')
    order = models.BigIntegerField()
    description = models.CharField(max_length=64)
    id_detail_catalogue = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'detail_catalogue'
    def __str__(self):
        return str(self.description)

class GameLog(models.Model):
    id_game_log = models.AutoField(primary_key=True)
    id_gamer_fk = models.ForeignKey('GamerTournament', models.CASCADE, db_column='id_gamer_fk')
    id_tournament_fk = models.BigIntegerField()
    id_question_fk = models.ForeignKey('Question', models.CASCADE, db_column='id_question_fk')
    id_answer_fk = models.ForeignKey(Answer, models.CASCADE, db_column='id_answer_fk')
    is_valid = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'game_log'
    def __str__(self):
        return str(self.id_game_log)

class Gamer(models.Model):
    identification = models.CharField(primary_key=True, max_length=15)
    username = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    credits = models.BigIntegerField()  # This field type is a guess.
    loginstate = models.BigIntegerField()
    user_type_fk = models.ForeignKey(DetailCatalogue, models.CASCADE, db_column='user_type_fk')

    class Meta:
        managed = False
        db_table = 'gamer'
    def __str__(self):
        return str(self.username)

class GamerTournament(models.Model):
    id_gamer_fk = models.OneToOneField(Gamer, models.CASCADE, db_column='id_gamer_fk', primary_key=True)
    id_tournament_fk = models.ForeignKey('Tournament', models.CASCADE, db_column='id_tournament_fk')

    class Meta:
        managed = False
        db_table = 'gamer_tournament'
        unique_together = (('id_gamer_fk', 'id_tournament_fk'),)
    def __str__(self):
        return str(self.id_gamer_fk)+'-'+str(self.id_gamer_fk)

class MasterCatalogue(models.Model):
    id_master_catalogue = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'master_catalogue'
    def __str__(self):
        return str(self.name)

class Purchases(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    id_gamer_fk = models.ForeignKey(Gamer, models.CASCADE, db_column='id_gamer_fk')
    purchase_date = models.DateTimeField()
    num_credits = models.BigIntegerField()
    payment_type_fk = models.ForeignKey(DetailCatalogue, models.CASCADE, db_column='payment_type_fk')

    class Meta:
        managed = False
        db_table = 'purchases'
    def __str__(self):
        return str(self.id_purchase)

class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=128)
    id_tournament_subject_fk = models.ForeignKey('TournamentSubject', models.CASCADE, db_column='id_tournament_subject_fk')

    class Meta:
        managed = False
        db_table = 'question'
    def __str__(self):
        return str(self.question_text)

class Tournament(models.Model):
    id_tournament = models.AutoField(primary_key=True)
    id_tournament_subject_fk = models.ForeignKey('TournamentSubject', models.CASCADE, db_column='id_tournament_subject_fk')
    game_date = models.DateField()
    game_start = models.DateTimeField()
    game_end = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tournament'
    def __str__(self):
        return str(self.id_tournament)

class TournamentSubject(models.Model):
    id_tournament_subject = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'tournament_subject'
    def __str__(self) -> str:
        return str(self.description)

class Winner(models.Model):
    id_gamer_fk = models.ForeignKey(Gamer, models.CASCADE, db_column='id_gamer_fk')
    id_tournament_fk = models.ForeignKey(Tournament, models.CASCADE, db_column='id_tournament_fk')
    position = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'winner'
    def __str__(self):
        return str(self.id_gamer_fk)