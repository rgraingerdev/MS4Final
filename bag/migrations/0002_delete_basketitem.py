# Generated by Django 5.0.2 on 2024-02-22 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bag", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BasketItem",
        ),
    ]