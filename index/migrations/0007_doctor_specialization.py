# Generated by Django 5.1.1 on 2024-10-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0006_hospital_doctor"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="specialization",
            field=models.CharField(default="", max_length=40),
        ),
    ]
