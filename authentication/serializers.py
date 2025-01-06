from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        errors = {}
        
        # Check for existing username
        if User.objects.filter(username=attrs['username']).exists():
            errors['username'] = 'A user with this username already exists.'
        
        # Check for existing email
        if User.objects.filter(email=attrs['email']).exists():
            errors['email'] = 'A user with this email already exists.'
        
        # Check for existing phone number
        if User.objects.filter(phone_number=attrs['phone_number']).exists():
            errors['phone_number'] = 'A user with this phone number already exists.'

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
