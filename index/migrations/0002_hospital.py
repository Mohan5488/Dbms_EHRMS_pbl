# Generated by Django 5.1.1 on 2024-10-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hospital",
            fields=[
                (
                    "hid",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("hname", models.CharField(max_length=25)),
                ("haddr", models.CharField(max_length=100)),
            ],
        ),
    ]
