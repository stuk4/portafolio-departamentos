# Generated by Django 3.1 on 2020-12-14 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_user_n_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='N_tarjeta',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(16)]),
        ),
    ]