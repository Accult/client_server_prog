# Generated by Django 4.2.11 on 2024-03-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(choices=[("male", "Male"), ("female", "Female")], default="male", max_length=6),
        ),
    ]
