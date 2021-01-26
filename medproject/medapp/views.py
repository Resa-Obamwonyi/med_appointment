from django.db import transaction
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import AllowAny
from .lib.lower_strip import strip_and_lower
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor, Patient, Availability, Appointment
# from rest_framework.authtoken.models import Token


# Login View
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # try:
        #     email = strip_and_lower(request.data.get('email', ''))
        #     password = request.data.get('password', '')
        #
        #     if email is None or password is None:
        #         return Response(
        #             dict(invalid_credential='Please provide both email and password'),
        #             status=status.HTTP_400_BAD_REQUEST)
        #     try:
        #         db_user = Doctor.objects.get(email=email)
        #         # db_user = Patient.objects.get(email=email)
        #
        #     except Exception:
        #         return Response(
        #             dict(invalid_credential='This Email does not exist in our records'),
        #             status=status.HTTP_400_BAD_REQUEST)
        #
        #     user = check_password(password, db_user.password)
        #
        #     if not user:
        #         return Response(
        #             dict(invalid_credential='Please ensure that your email and password are correct'),
        #             status=status.HTTP_400_BAD_REQUEST)
        #
        #     token, _ = Token.objects.get_or_create(user=db_user)
        #     return Response(dict(token=token.key), status=status.HTTP_200_OK)
        #
        # except Exception as err:
        #     return Response(dict(error=err), status=status.HTTP_400_BAD_REQUEST)
        return  Response(
           dict(success="Login Page")
        )