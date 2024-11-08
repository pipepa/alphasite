# Generated by Django 5.1 on 2024-11-01 12:54

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firework', '0010_alter_shells_color_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fireposition',
            options={'verbose_name': 'вогнева позиція', 'verbose_name_plural': 'вогневі позиції'},
        ),
        migrations.AlterModelOptions(
            name='tablesfire',
            options={'verbose_name': 'залежність', 'verbose_name_plural': 'залежності'},
        ),
        migrations.AlterField(
            model_name='shells',
            name='color',
            field=colorfield.fields.ColorField(default='4eb78f', image_field=None, max_length=25, samples=None, verbose_name='Колір'),
        ),
        migrations.AlterField(
            model_name='tablesfire',
            name='number_powder',
            field=models.CharField(choices=[('Без номеру', 'Без номеру'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default='Без номеру', max_length=50, verbose_name='Номер заряду'),
        ),
    ]
