# Generated by Django 4.1.5 on 2023-05-08 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ref_dom_btp', '0003_domaine_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('description', models.TextField()),
                ('lieux', models.CharField(max_length=100)),
                ('statut', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_domaine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domaine_offre', to='ref_dom_btp.domaine')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('code', models.CharField(max_length=60, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_appreciation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_apprecier', to='gest_offres.appreciation')),
                ('id_offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_doffre', to='gest_offres.offre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reserve', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ouvrier_reserver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='offre',
            name='id_reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offre_reserver', to='gest_offres.reservation'),
        ),
        migrations.AddField(
            model_name='offre',
            name='id_travaux',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offre_travaux', to='ref_dom_btp.travaux'),
        ),
        migrations.AddField(
            model_name='offre',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_doffre', to='gest_offres.offre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appreciation',
            name='id_reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appreciation_reserver', to='gest_offres.reservation'),
        ),
    ]