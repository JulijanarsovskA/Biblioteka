# Generated by Django 4.0.4 on 2022-05-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbiblioteka', '0003_remove_knigi_elektronski_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='knigi',
            name='elektronski_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
