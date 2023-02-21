from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','username','password', 'password2', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        """
            A method overiding DRF serializer's save method
        """
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()

        return user