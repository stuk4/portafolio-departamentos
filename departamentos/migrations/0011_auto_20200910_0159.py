# Generated by Django 3.1 on 2020-09-10 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0010_auto_20200908_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='mantencion',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
