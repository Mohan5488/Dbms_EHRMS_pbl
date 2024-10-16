# Generated by Django 5.1.1 on 2024-10-08 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
        ("index", "0007_doctor_specialization"),
    ]

    operations = [
        migrations.CreateModel(
            name="appointment",
            fields=[
                (
                    "aid",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("doa", models.DateField()),
                ("mobile", models.BigIntegerField()),
                ("message", models.CharField(max_length=100)),
                (
                    "did",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="index.doctor"
                    ),
                ),
            ],
        ),
    ]
