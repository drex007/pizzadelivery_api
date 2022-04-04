from .models import User 
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from getpass import getpass

class UserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank= False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    
    
    def validate(self, attributes):
        username_exists = User.objects.filter(username = attributes['username'] ).exists()
        phone_exists = User.objects.filter(phone_number = attributes['phone_number']).exists()
        email_exists = User.objects.filter(email = attributes['email']).exists()
        
        if username_exists or  phone_exists or email_exists:
            raise serializers.ValidationError(detail="Username or Phone Number or Email already Exists")
        return super().validate(attributes)

    def create(self, validates_data):
        password = validates_data.pop('password', None)
        instance = self.Meta.model(**validates_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    
    def create(self, validates_data):
        password = validates_data.pop('password', None)
        instance = self.Meta.model(**validates_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(max_length=80)
    password = serializers.CharField(min_length=8)
    class Meta:
        model = User
        fields = ['id', 'username','password']
        extra_kwargs = {
            'password': {'write_only':True}
        }

      
    
