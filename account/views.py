from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer

from django.contrib.auth import login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from .models import User
import json


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    """
        An API view to regiister a user
    """
    data = {}
    try:
        #   Get all payload data
        user_data = {}
        user_data['email'] = request.data['email']
        user_data['first_name'] = request.data['first_name']
        user_data['last_name'] = request.data['last_name']
        user_data['password'] = request.data['password']
        user_data['password2'] = request.data['password2']
        user_data['username'] = request.data['username']

        message = "user registered successfully"
        serializer = RegisterSerializer(data=user_data)

        #   Check if serializer is valid
        if serializer.is_valid():
            account = serializer.save()
            account.save()
        else:
            data = serializer.errors
        #   create user token
        token = Token.objects.get_or_create(user=account)
        #   dict values to return as response
        data["message"] = message
        data["email"] = account.email
        data["username"] = account.username
        data['first_name'] = account.first_name
        data['last_name'] = account.last_name
        #   return response
        return Response(data)
    except Exception as e:
        print(e)
        message = {"error": "issue creating user"}
        return Response(status=status.HTTP_400_BAD_REQUEST, data=message)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    """
        A Login API view for users
    """

    data = {}
    #   get payloads
    req_body = json.loads(request.body)
    email = req_body['email']
    password = req_body['password']
    #   check if user has an account
    try:
        account = User.objects.get(email=email)
    except BaseException as e:
        raise ValidationError({"400": f'{str(e)}'})
    #   get or create user token
    token = Token.objects.get_or_create(user=account)[0].key

    #   check if passwords match
    if not check_password(password, account.password):
        return Response(
                {"error": "Incorrect Login credentials"}, 
                status=status.HTTP_404_NOT_FOUND
            )
    #   return user info if account exists
    if account:
        login(request, account)
        data["message"] = "user logged in"
        data["email_address"] = account.email

        result = {"data": data, "token": token}
        return Response(result)

    else:
        raise ValidationError({"400": f'Account doesnt exist'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """
        API to logout a user
    """
    #   if user is authenticated delete user token
    request.user.auth_token.delete()
    #   logout user
    logout(request)
    return Response({'message': 'User logged out successfully'})