# Generated by Django 5.0.2 on 2024-02-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.CharField(blank=True, max_length=254),
        ),
    ]