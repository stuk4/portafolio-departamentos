# Generated by Django 3.1 on 2020-10-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0010_auto_20201019_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='dia',
            field=models.CharField(default='Lunes', max_length=50),
        ),
    ]
