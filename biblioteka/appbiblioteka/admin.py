from django.contrib import admin
from .models import Knigi, Clen
from django.utils.timezone import now 
from datetime import timedelta
from twilio.rest import Client
import smtplib
import ssl

# Register your models here.

@admin.action(description="Notify user by SMS")
def notify_sms(modeladmin, request, queryset):
    account_sid = 'AC9788ddc354fd7c90ad30d692a843e635'
    auth_token = '1115cd5d8897910c17aaf6f536f0ae07'
    client = Client(account_sid, auth_token)
    for user in queryset:
        client.messages \
        .create(
            from_='+19894364864',
            body='Pocituvan {}, ve molime vratete ja knigata {} koja e pozajmena na {}'.format(user.ime, user.pozajmena_kniga.naslov, user.data_pozajmuvanje),
            to=user.telefon
    )

@admin.action(description="Notify user by EMAIL")
def notify_email(modeladmin, request, queryset):
    #login podatoci
    smtp_server = 'smtp.gmail.com'
    sender = 'sergeylange1@gmail.com'
    pwd = "lbzdsubmltzhdhyz"
    port = 465

    #ssl_enkripcija
    ssl_conn = ssl.create_default_context()
    for user in queryset:
        body='Pocituvan {}, ve molime vratete ja knigata {} koja e pozajmena na {}'.format(user.ime, user.pozajmena_kniga.naslov, user.data_pozajmuvanje),
    #konekcija so smpt server
        with smtplib.SMTP_SSL(smtp_server, port, context = ssl_conn) as server:
            server.login(sender, pwd)
            server.sendmail(sender, user.email, body)  
 

class ClenAdmin(admin.ModelAdmin):
    
    @admin.display(ordering = 'data_pozajmuvanje', description = 'denovi pozajmena')
    def denovi_pozajmena_kniga(self, obj):
        if obj.data_pozajmuvanje != None:
            return (now() - obj.data_pozajmuvanje).days
        else:
            return 

    list_display = ('id',"ime", "prezime", "telefon", "email", "data_clenstvo", "br_clenska_karta", "aktiven", "datum_clanarina_posledno", "data_pozajmuvanje", "dali_pozajmeno", 'pozajmena_kniga', "denovi_pozajmena_kniga")
    list_filter = ("data_clenstvo", "aktiven", "dali_pozajmeno", "data_pozajmuvanje")
    search_fields = ("ime", "prezime")
    actions = (notify_sms, notify_email)

class KnigiAdmin(admin.ModelAdmin):
    list_display = ('id',"naslov", "avtor", "zanr", "kolicina", "izdavacka_kukja", "elektronska_verzija", "elektronski_file", "cena")
    list_filter = ("zanr", "avtor", "izdavacka_kukja")
    search_fields = ("naslov", "avtor")

admin.site.register(Knigi, KnigiAdmin)
admin.site.register(Clen, ClenAdmin)

