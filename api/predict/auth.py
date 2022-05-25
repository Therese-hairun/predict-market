from django.contrib.auth.models import User
import jwt, os
from rest_framework import authentication, exceptions, status
from .models import Client


class Unauthorized(exceptions.APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Unauthorized."
    default_code = "not_authenticated"


class TokenExpired(exceptions.APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Token expired."
    default_code = "Not_authenticated"


class BasicAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header_value = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header_value:
            authmeth, auth = request.META["HTTP_AUTHORIZATION"].split(" ", 1)
            if not auth:
                return None
            if not authmeth.lower() == "bearer":
                return None
            try:
                token = jwt.decode(
                    auth, os.environ.get("SECRET_KEY"), algorithms="HS256"
                )
            except jwt.ExpiredSignatureError:
                raise TokenExpired()
            except jwt.InvalidSignatureError:
                raise Unauthorized(detail="Invalid Token")
            return (token, None)
        else:
            raise Unauthorized()


class AdminAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header_value = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header_value:
            authmeth, auth = request.META["HTTP_AUTHORIZATION"].split(" ", 1)
            if not auth:
                return None
            if not authmeth.lower() == "bearer":
                return None
            try:
                token = jwt.decode(
                    auth, os.environ.get("SECRET_KEY"), algorithms="HS256"
                )
            except jwt.ExpiredSignatureError:
                raise TokenExpired()
            except jwt.InvalidSignatureError:
                raise Unauthorized(detail="Invalid Token")
            if "admin_id" in token:
                return (token, None)
            raise Unauthorized()
        else:
            raise Unauthorized()
