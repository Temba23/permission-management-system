from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=CustomUser.objects.all())]
  )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2',
            'email', 'number', 'dob')
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        number=validated_data['number'],
        dob=validated_data['dob'],
        role='User'
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
