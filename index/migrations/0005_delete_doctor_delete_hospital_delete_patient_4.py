# Generated by Django 5.1.1 on 2024-10-08 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0004_doctor"),
    ]

    operations = [
        migrations.DeleteModel(
            name="doctor",
        ),
        migrations.DeleteModel(
            name="Hospital",
        ),
        migrations.DeleteModel(
            name="patient_4",
        ),
    ]
