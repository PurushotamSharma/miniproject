# Generated by Django 4.2.6 on 2023-11-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_order_orderitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact_page",
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
                ("your_name", models.CharField(max_length=150)),
                ("Email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=150)),
                ("text", models.TextField(max_length=500)),
            ],
        ),
    ]
