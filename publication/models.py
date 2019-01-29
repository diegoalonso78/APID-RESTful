from django.db import models

class Paper(models.Model):
    pubmed_id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    journal = models.CharField(max_length=250, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper'

