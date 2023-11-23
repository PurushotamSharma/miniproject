# Generated by Django 4.2.6 on 2023-11-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pay",
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
                ("name", models.CharField(blank=True, max_length=1000)),
                ("amount", models.CharField(blank=True, max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("order_id", models.CharField(max_length=1000)),
                ("paid", models.BooleanField(default=False)),
            ],
        ),
    ]
