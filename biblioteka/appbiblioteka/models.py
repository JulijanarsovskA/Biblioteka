from django.db import models

# Create your models here.
class Knigi(models.Model):
    naslov = models.CharField(max_length = 50, unique = True)
    avtor = models.CharField(max_length = 50)
    zanr = models.CharField(max_length = 50)
    godina_izdavanje = models.IntegerField()
    kolicina = models.IntegerField()
    lokacija = models.CharField(max_length = 50)
    izdavacka_kukja = models.CharField(max_length = 50)
    jazik = models.CharField(max_length = 50)
    br_strani = models.IntegerField()
    elektronska_verzija = models.BooleanField()
    elektronski_file = models.FileField(null=True, blank=True)
    ISBN = models.CharField(max_length = 50)
    naslov_original = models.CharField(max_length = 50)
    cena = models.FloatField()
    kaznena_cena = models.FloatField()
    dali_e_prevedena = models.BooleanField()

class Clen(models.Model):
    ime = models.CharField(max_length = 50)
    prezime = models.CharField(max_length = 50)
    data_clenstvo = models.DateField()
    br_clenska_karta = models.IntegerField()
    telefon = models.CharField(max_length = 50)
    adresa = models.CharField(max_length = 50)
    data_raganje = models.DateField()
    aktiven = models.BooleanField()
    datum_clanarina_posledno = models.DateField()
    dali_pozajmeno = models.BooleanField()
    pozajmena_kniga = models.ForeignKey(Knigi, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=50, null = True, blank = True)
    data_pozajmuvanje = models.DateTimeField(null = True, blank = True)



