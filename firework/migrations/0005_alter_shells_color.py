# Generated by Django 5.1 on 2024-11-01 11:00

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firework', '0004_alter_shells_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shells',
            name='color',
            field=colorfield.fields.ColorField(default='04e057', image_field=None, max_length=25, samples=None, verbose_name='Колір'),
        ),
    ]
