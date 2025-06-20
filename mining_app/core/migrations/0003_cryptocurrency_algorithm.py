# Generated by Django 5.2.1 on 2025-06-15 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_hashrates"),
    ]

    operations = [
        migrations.AddField(
            model_name="cryptocurrency",
            name="algorithm",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cryptocurrencies",
                to="core.algorithm",
            ),
        ),
    ]
