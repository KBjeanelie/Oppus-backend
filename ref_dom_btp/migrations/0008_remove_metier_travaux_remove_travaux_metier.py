# Generated by Django 4.1.5 on 2023-07-07 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ref_dom_btp', '0007_metier_travaux_alter_travaux_metier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metier',
            name='travaux',
        ),
        migrations.RemoveField(
            model_name='travaux',
            name='metier',
        ),
    ]
