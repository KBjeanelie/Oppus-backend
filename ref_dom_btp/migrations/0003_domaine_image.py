# Generated by Django 4.1.5 on 2023-03-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_dom_btp', '0002_metier'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='domaine_img/'),
        ),
    ]