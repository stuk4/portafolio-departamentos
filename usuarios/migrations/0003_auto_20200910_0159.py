# Generated by Django 3.1 on 2020-09-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20200910_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]