# Generated by Django 4.1.5 on 2023-06-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_offres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]