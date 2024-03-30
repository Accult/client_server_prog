from django.db import models


class User(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="male")

    def __str__(self):
        return self.first_name
