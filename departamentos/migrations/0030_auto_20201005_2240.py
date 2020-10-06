# Generated by Django 3.1 on 2020-10-06 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0029_auto_20201002_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arriendo',
            name='diferencia',
        ),
        migrations.RemoveField(
            model_name='arriendo',
            name='total',
        ),
        migrations.AddField(
            model_name='check_in',
            name='diferencia',
            field=models.PositiveIntegerField(default=270000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check_in',
            name='total',
            field=models.PositiveIntegerField(default=300000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check_out',
            name='total',
            field=models.PositiveIntegerField(default=300000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check_out',
            name='valor_danos',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check_out',
            name='valor_tours',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check_out',
            name='valor_transporte',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
