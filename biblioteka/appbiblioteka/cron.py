from .models import Clen
from django.utils.timezone import now
from twilio.rest import Client

def send_sms():
    clenovi = Clen.objects.all()
    for clen in clenovi:
        denovi_pozajmena = (now() - clen.data_pozajmuvanje).days
        denovi_potsetuvanje = clen.denovi_potsetuvanje
        if denovi_pozajmena