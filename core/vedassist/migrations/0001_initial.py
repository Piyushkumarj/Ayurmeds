# Generated by Django 4.1.7 on 2023-05-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AyurvedicPrediction",
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
                ("cold", models.IntegerField()),
                ("eyepain", models.IntegerField()),
                ("fever", models.IntegerField()),
                ("headache", models.IntegerField()),
                ("stomachache", models.IntegerField()),
                ("dizziness", models.IntegerField()),
                ("vomiting", models.IntegerField()),
                ("chestpain", models.IntegerField()),
                ("jointpain", models.IntegerField()),
                ("loosemotion", models.IntegerField()),
                ("throatinfection", models.IntegerField()),
                ("age", models.IntegerField()),
                ("gender", models.IntegerField()),
                ("weight", models.IntegerField()),
                ("medicine1", models.CharField(max_length=100)),
                ("medicine2", models.CharField(max_length=100)),
                ("medicine3", models.CharField(max_length=100)),
            ],
        ),
    ]