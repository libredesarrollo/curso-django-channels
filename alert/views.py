from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    try: 
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido ",status=status.HTTP_401_UNAUTHORIZED)

    pwd_valid = check_password(password,user.password)

    if not pwd_valid:
        return Response("Contraseña inválida",status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)

    return Response("Token_"+token.key)