# Generated by Django 4.2.11 on 2024-03-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_user_gender_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(choices=[("m", "Male"), ("f", "Female")], default="M", max_length=1),
        ),
    ]