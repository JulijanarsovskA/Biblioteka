# Generated by Django 4.0.4 on 2022-05-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbiblioteka', '0006_rename_vk_kolicina_knigi_kolicina'),
    ]

    operations = [
        migrations.AddField(
            model_name='clen',
            name='data_pozajmuvanje',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='clen',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]