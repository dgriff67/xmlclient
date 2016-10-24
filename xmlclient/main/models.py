from django.db import models

# Create your models here.
class Pl1516(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField
    resource_uri = models.TextField(db_column='resource_uri', blank=True, null=True)
    div = models.TextField(db_column='Div', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hometeam = models.TextField(db_column='HomeTeam', blank=True, null=True)  # Field name made lowercase.
    awayteam = models.TextField(db_column='AwayTeam', blank=True, null=True)  # Field name made lowercase.
    fthg = models.IntegerField(db_column='FTHG', blank=True, null=True)  # Field name made lowercase.
    ftag = models.IntegerField(db_column='FTAG', blank=True, null=True)  # Field name made lowercase.
    ftr = models.TextField(db_column='FTR', blank=True, null=True)  # Field name made lowercase.
    hthg = models.IntegerField(db_column='HTHG', blank=True, null=True)  # Field name made lowercase.
    htag = models.IntegerField(db_column='HTAG', blank=True, null=True)  # Field name made lowercase.
    htr = models.TextField(db_column='HTR', blank=True, null=True)  # Field name made lowercase.
    referee = models.TextField(db_column='Referee', blank=True, null=True)  # Field name made lowercase.
    hs = models.IntegerField(db_column='HS', blank=True, null=True)  # Field name made lowercase.
    as_field = models.IntegerField(db_column='AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    hst = models.IntegerField(db_column='HST', blank=True, null=True)  # Field name made lowercase.
    ast = models.IntegerField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    hf = models.IntegerField(db_column='HF', blank=True, null=True)  # Field name made lowercase.
    af = models.IntegerField(db_column='AF', blank=True, null=True)  # Field name made lowercase.
    hc = models.IntegerField(db_column='HC', blank=True, null=True)  # Field name made lowercase.
    ac = models.IntegerField(db_column='AC', blank=True, null=True)  # Field name made lowercase.
    hy = models.IntegerField(db_column='HY', blank=True, null=True)  # Field name made lowercase.
    ay = models.IntegerField(db_column='AY', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    ar = models.IntegerField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    b365h = models.FloatField(db_column='B365H', blank=True, null=True)  # Field name made lowercase.
    b365d = models.FloatField(db_column='B365D', blank=True, null=True)  # Field name made lowercase.
    b365a = models.FloatField(db_column='B365A', blank=True, null=True)  # Field name made lowercase.
    bwh = models.FloatField(db_column='BWH', blank=True, null=True)  # Field name made lowercase.
    bwd = models.FloatField(db_column='BWD', blank=True, null=True)  # Field name made lowercase.
    bwa = models.FloatField(db_column='BWA', blank=True, null=True)  # Field name made lowercase.
    iwh = models.FloatField(db_column='IWH', blank=True, null=True)  # Field name made lowercase.
    iwd = models.FloatField(db_column='IWD', blank=True, null=True)  # Field name made lowercase.
    iwa = models.FloatField(db_column='IWA', blank=True, null=True)  # Field name made lowercase.
    lbh = models.FloatField(db_column='LBH', blank=True, null=True)  # Field name made lowercase.
    lbd = models.FloatField(db_column='LBD', blank=True, null=True)  # Field name made lowercase.
    lba = models.FloatField(db_column='LBA', blank=True, null=True)  # Field name made lowercase.
    psh = models.FloatField(db_column='PSH', blank=True, null=True)  # Field name made lowercase.
    psd = models.FloatField(db_column='PSD', blank=True, null=True)  # Field name made lowercase.
    psa = models.FloatField(db_column='PSA', blank=True, null=True)  # Field name made lowercase.
    whh = models.FloatField(db_column='WHH', blank=True, null=True)  # Field name made lowercase.
    whd = models.FloatField(db_column='WHD', blank=True, null=True)  # Field name made lowercase.
    wha = models.FloatField(db_column='WHA', blank=True, null=True)  # Field name made lowercase.
    vch = models.FloatField(db_column='VCH', blank=True, null=True)  # Field name made lowercase.
    vcd = models.FloatField(db_column='VCD', blank=True, null=True)  # Field name made lowercase.
    vca = models.FloatField(db_column='VCA', blank=True, null=True)  # Field name made lowercase.
    bb1x2 = models.FloatField(db_column='Bb1X2', blank=True, null=True)  # Field name made lowercase.
    bbmxh = models.FloatField(db_column='BbMxH', blank=True, null=True)  # Field name made lowercase.
    bbavh = models.FloatField(db_column='BbAvH', blank=True, null=True)  # Field name made lowercase.
    bbmxd = models.FloatField(db_column='BbMxD', blank=True, null=True)  # Field name made lowercase.
    bbavd = models.FloatField(db_column='BbAvD', blank=True, null=True)  # Field name made lowercase.
    bbmxa = models.FloatField(db_column='BbMxA', blank=True, null=True)  # Field name made lowercase.
    bbava = models.FloatField(db_column='BbAvA', blank=True, null=True)  # Field name made lowercase.
    bbou = models.FloatField(db_column='BbOU', blank=True, null=True)  # Field name made lowercase.
    bbmx_2_5 = models.FloatField(db_column='BbMx>2.5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bbav_2_5 = models.FloatField(db_column='BbAv>2.5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bbmx_2_5_0 = models.FloatField(db_column='BbMx<2.5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    bbav_2_5_0 = models.FloatField(db_column='BbAv<2.5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    bbah = models.FloatField(db_column='BbAH', blank=True, null=True)  # Field name made lowercase.
    bbahh = models.FloatField(db_column='BbAHh', blank=True, null=True)  # Field name made lowercase.
    bbmxahh = models.FloatField(db_column='BbMxAHH', blank=True, null=True)  # Field name made lowercase.
    bbavahh = models.FloatField(db_column='BbAvAHH', blank=True, null=True)  # Field name made lowercase.
    bbmxaha = models.FloatField(db_column='BbMxAHA', blank=True, null=True)  # Field name made lowercase.
    bbavaha = models.FloatField(db_column='BbAvAHA', blank=True, null=True)  # Field name made lowercase.
    psch = models.FloatField(db_column='PSCH', blank=True, null=True)  # Field name made lowercase.
    pscd = models.FloatField(db_column='PSCD', blank=True, null=True)  # Field name made lowercase.
    psca = models.FloatField(db_column='PSCA', blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return "{0} {1} vs {2} {3} on {4}".format(self.hometeam, self.fthg, self.awayteam, self.ftag, self.date)

