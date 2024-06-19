# Generated by Django 5.0.6 on 2024-06-19 08:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faunatrack", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="espece",
            name="nom_commun",
        ),
        migrations.AddField(
            model_name="espece",
            name="nom",
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="espece",
            name="status",
            field=models.CharField(
                choices=[("danger", "Danger"), ("hors de danger", "Sain")],
                default="hors de danger",
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="Observation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("quantite", models.IntegerField(default=1)),
                ("notes", models.TextField(blank=True, default=None, null=True)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="obs_photos/"),
                ),
                (
                    "espece",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="observations",
                        to="faunatrack.espece",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Projet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, default=None, null=True)),
                ("slug", models.SlugField(blank=True)),
                (
                    "observations",
                    models.ManyToManyField(
                        related_name="projets", to="faunatrack.observation"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Scientifique",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("universite", models.CharField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="observation",
            name="scientifique",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="observations",
                to="faunatrack.scientifique",
            ),
        ),
    ]
