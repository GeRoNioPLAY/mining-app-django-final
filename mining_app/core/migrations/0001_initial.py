# Generated by Django 5.2.1 on 2025-05-30 19:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Algorithm",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="algorithms",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Алгоритм",
                "verbose_name_plural": "Алгоритмы",
            },
        ),
        migrations.CreateModel(
            name="Cryptocurrency",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32, unique=True)),
                ("network_difficulty", models.FloatField()),
                ("block_reward", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cryptocurrencies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Криптовалюта",
                "verbose_name_plural": "Криптовалюты",
            },
        ),
        migrations.CreateModel(
            name="Device",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("company", models.CharField(max_length=32)),
                ("name", models.CharField(max_length=32)),
                ("cost", models.FloatField()),
                ("power_consumption", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="devices",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Устройство",
                "verbose_name_plural": "Устройства",
            },
        ),
        migrations.CreateModel(
            name="Exchange",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="exchanges",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Биржа",
                "verbose_name_plural": "Биржи",
            },
        ),
        migrations.CreateModel(
            name="CryptocurrencyPrice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cryptocurrency_prices",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "cryptocurrency",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="prices",
                        to="core.cryptocurrency",
                    ),
                ),
                (
                    "exchange",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="prices",
                        to="core.exchange",
                    ),
                ),
            ],
            options={
                "verbose_name": "Цена криптовалюты",
                "verbose_name_plural": "Цены криптовалют",
            },
        ),
        migrations.CreateModel(
            name="Mining",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("hashrate", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "algorithm",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mining_sessions",
                        to="core.algorithm",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mining_sessions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "cryptocurrency",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mining_sessions",
                        to="core.cryptocurrency",
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mining_sessions",
                        to="core.device",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сессия майнинга",
                "verbose_name_plural": "Сессии майнинга",
            },
        ),
    ]
