# Generated by Django 4.0.4 on 2022-05-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbiblioteka', '0007_clen_data_pozajmuvanje_clen_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clen',
            name='data_pozajmuvanje',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
