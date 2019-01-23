# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bioplex(models.Model):
    genea = models.CharField(db_column='GeneA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    geneb = models.CharField(db_column='GeneB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uniprota = models.CharField(db_column='UniprotA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uniprotb = models.CharField(db_column='UniprotB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    symbola = models.CharField(db_column='SymbolA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    symbolb = models.CharField(db_column='SymbolB', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bioplex'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Geneontology(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    uniprotid = models.CharField(max_length=10)
    ontology = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geneontology'
        unique_together = (('id', 'uniprotid'),)


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
        
        db_table = 'interaction'

    def __str__(self):
        return self.participant1 + '-' + self.participant2


class Interpro(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    uniprotid = models.CharField(max_length=10)
    family = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interpro'
        unique_together = (('id', 'uniprotid'),)


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


class Method(models.Model):
    psimi_id = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'method'


class Paper(models.Model):
    pubmed_id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    journal = models.CharField(max_length=250, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper'


class Pdbinterfaces(models.Model):
    pdbid = models.CharField(db_column='pdbId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    interaction = models.IntegerField(blank=True, null=True)
    chain1 = models.CharField(max_length=15, blank=True, null=True)
    chain2 = models.CharField(max_length=15, blank=True, null=True)
    residues = models.CharField(max_length=10, blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    salt = models.IntegerField(blank=True, null=True)
    disulphide = models.IntegerField(blank=True, null=True)
    hydrogen = models.IntegerField(blank=True, null=True)
    nonbonded = models.IntegerField(db_column='nonBonded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdbinterfaces'


class Pdbuniprot(models.Model):
    pdbid = models.CharField(db_column='pdbID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chain = models.CharField(max_length=1, blank=True, null=True)
    uniprotid = models.CharField(db_column='uniprotID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdbuniprot'


class Pfam(models.Model):
    id = models.CharField(primary_key=True, max_length=7)
    uniprotid = models.CharField(max_length=10)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pfam'
        unique_together = (('id', 'uniprotid'),)


class Ppimethods(models.Model):
    psi_mi_id = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    mi_type = models.CharField(max_length=255, blank=True, null=True)
    meta_id = models.IntegerField(blank=True, null=True)
    meta_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppimethods'


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


class Proteomes(models.Model):
    proteome_id = models.CharField(primary_key=True, max_length=255)
    organism = models.CharField(max_length=255, blank=True, null=True)
    taxon_id = models.IntegerField(blank=True, null=True)
    proteins = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proteomes'


class ProteomesAnterior(models.Model):
    proteome_id = models.CharField(primary_key=True, max_length=255)
    organism = models.CharField(max_length=255, blank=True, null=True)
    taxon_id = models.IntegerField(blank=True, null=True)
    proteins = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proteomes_anterior'


class Reactome(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    uniprotid = models.CharField(max_length=10)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reactome'
        unique_together = (('id', 'uniprotid'),)


class Taxon(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    proteome = models.IntegerField(blank=True, null=True)
    reviewed = models.CharField(max_length=20, blank=True, null=True)
    interactions1 = models.IntegerField(blank=True, null=True)
    interactingproteins1 = models.IntegerField(blank=True, null=True)
    interactions2 = models.IntegerField(blank=True, null=True)
    interactingproteins2 = models.IntegerField(blank=True, null=True)
    interactions3 = models.IntegerField(blank=True, null=True)
    interactingproteins3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxon'


class TaxonAntesEe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    proteome = models.IntegerField(blank=True, null=True)
    reviewed = models.CharField(max_length=20, blank=True, null=True)
    interactions1 = models.IntegerField(blank=True, null=True)
    interactingproteins1 = models.IntegerField(blank=True, null=True)
    interactions2 = models.IntegerField(blank=True, null=True)
    interactingproteins2 = models.IntegerField(blank=True, null=True)
    interactions3 = models.IntegerField(blank=True, null=True)
    interactingproteins3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxon_antes_ee'


class Uniprotid(models.Model):
    current_id = models.CharField(primary_key=True, max_length=15)
    deprecated_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'uniprotid'
        unique_together = (('current_id', 'deprecated_id'),)
