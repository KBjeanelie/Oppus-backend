# Generated by Django 4.1.5 on 2023-06-01 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ref_dom_btp', '0003_domaine_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='metier',
            name='travaux',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ref_dom_btp.travaux'),
        ),
    ]
