# Generated by Django 3.1 on 2020-10-14 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0003_auto_20201013_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='zona',
            field=models.CharField(choices=[('Sur', 'Sur'), ('Este', 'Este'), ('Oeste', 'Oeste'), ('Norte', 'Norte')], default='Sur', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='dia',
            field=models.CharField(default=datetime.date(2020, 10, 14), max_length=50),
        ),
    ]
