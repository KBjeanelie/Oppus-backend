# Generated by Django 4.1.5 on 2023-04-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
