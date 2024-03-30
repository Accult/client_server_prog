from rest_framework import serializers
from core.models import User


def contains_digit_validator(value):
    if not value.isalpha():
        raise serializers.ValidationError("Field cannot contain digits or symbols")


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2, max_length=20, validators=[contains_digit_validator])
    last_name = serializers.CharField(min_length=2, max_length=20, validators=[contains_digit_validator])
    age = serializers.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "age"]
