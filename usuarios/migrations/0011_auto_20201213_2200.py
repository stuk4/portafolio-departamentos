# Generated by Django 3.1 on 2020-12-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20201213_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='N_tarjeta',
            field=models.BigIntegerField(null=True),
        ),
    ]
