from django.db import models

class Protein(models.Model):
    uniprot_id = models.CharField(max_length=30, blank=True, null=True)
    gene_id = models.CharField(max_length=12, blank=True, null=True)
    uniprot_name = models.CharField(max_length=45, blank=True, null=True)
    uniprot_desc = models.CharField(max_length=150, blank=True, null=True)
    taxon_id = models.PositiveIntegerField(blank=True, null=True)
    gene_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protein'

