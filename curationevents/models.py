from django.db import models

class Intmetpaper(models.Model):
    interaction = models.PositiveIntegerField(blank=True, null=True)
    method = models.PositiveIntegerField(blank=True, null=True)
    paper = models.IntegerField(blank=True, null=True)
    role1 = models.PositiveIntegerField(blank=True, null=True)
    role2 = models.PositiveIntegerField(blank=True, null=True)
    multiple = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    sourceid = models.CharField(db_column='sourceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mi_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intmetpaper'

class Interaction(models.Model):
    participant1 = models.CharField(max_length=15, blank=True, null=True)
    participant2 = models.CharField(max_length=15, blank=True, null=True)
    methods = models.PositiveIntegerField()
    papers = models.PositiveIntegerField()
    experiments = models.PositiveIntegerField()
    curationevents = models.PositiveIntegerField()
    intact = models.PositiveIntegerField()
    hprd = models.PositiveIntegerField()
    dip = models.PositiveIntegerField()
    biogrid = models.PositiveIntegerField()
    bioplex = models.PositiveIntegerField()
    pdb = models.IntegerField()
    participant1_uniprot_name = models.CharField(max_length=45, blank=True, null=True)
    participant2_uniprot_name = models.CharField(max_length=45, blank=True, null=True)
    participant1_taxon_id = models.PositiveIntegerField(blank=True, null=True)
    participant2_taxon_id = models.PositiveIntegerField(blank=True, null=True)
    ee = models.IntegerField(blank=True, null=True)
    mi_types = models.IntegerField(db_column='MI_types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        managed = False
        db_table = 'interaction'