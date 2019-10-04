# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class PmpAuditTesting(models.Model):
    #Sample Filed Name
    Name = models.CharField(max_length=128, blank=True, null=True)
    Comments = models.CharField(max_length=128, blank=True, null=True)
    School = models.CharField(max_length=128, blank=True, null=True)
    Graduation_year = models.BigIntegerField(blank=True, null=True)
       id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sample table name'
