# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asset(models.Model):
    id = models.BigAutoField(primary_key=True)
    assetname = models.CharField(
        db_column="assetName", unique=True, max_length=20
    )  # Field name made lowercase.
    assetfullname = models.CharField(
        db_column="assetFullname", max_length=50
    )  # Field name made lowercase.
    created = models.DateTimeField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = "asset"


class Symbol(models.Model):
    id = models.BigAutoField(primary_key=True)
    symbol = models.CharField(unique=True, max_length=20)
    baseasset = models.ForeignKey(
        Asset, models.DO_NOTHING, db_column="baseAsset", related_name="baseAsset"
    )  # Field name made lowercase.
    quoteasset = models.ForeignKey(
        Asset, models.DO_NOTHING, db_column="quoteAsset", related_name="quoteAsset"
    )  # Field name made lowercase.
    created = models.DateTimeField()
    usable = models.IntegerField()

    class Meta:
        managed = False
        db_table = "symbol"


class Training(models.Model):
    id = models.BigAutoField(primary_key=True)
    symbolid = models.ForeignKey(Symbol, models.DO_NOTHING, db_column="symbolid")
    intervaltime = models.CharField(max_length=6)
    tag = models.CharField(max_length=6)
    trainingstate = models.CharField(max_length=12)
    latesttrainingstarttime = models.DateTimeField()
    latesttrainingendtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "training"
