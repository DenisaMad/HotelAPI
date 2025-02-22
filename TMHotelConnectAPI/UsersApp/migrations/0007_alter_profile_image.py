# Generated by Django 4.2.6 on 2023-11-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UsersApp", "0006_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="placeholder.png", null=True, upload_to="images"
            ),
        ),
    ]
