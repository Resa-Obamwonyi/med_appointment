from rest_framework.permissions import AllowAny
from .lib.lower_strip import strip_and_lower
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor, Patient, Availability, Appointment


# Login View
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = strip_and_lower(request.data.get('email', ''))
            password = request.data.get('password', '')

            if email is None or password is None:
                return Response(
                    dict(invalid_credential='Please provide both email and password'),
                    status=status.HTTP_400_BAD_REQUEST)

            try:
                user_type = Doctor.objects.get(email=email)
            except Exception:
                user_type = Patient.objects.get(email=email)

            if isinstance(user_type, Doctor) and password == Doctor.objects.get(email=email).password:
                doctor = Doctor.objects.get(email=email)

                if not doctor:
                    return Response(
                        dict(invalid_credential='Please ensure that your email and password are correct'),
                        status=status.HTTP_400_BAD_REQUEST)

                return Response(dict(message=f"Welcome Doctor {doctor.first_name}"), status=status.HTTP_200_OK)

            if isinstance(user_type, Patient) and password == Patient.objects.get(email=email).password:
                patient = Patient.objects.get(email=email)

                if not patient:
                    return Response(
                        dict(invalid_credential='Please ensure that your email and password are correct'),
                        status=status.HTTP_400_BAD_REQUEST)

                return Response(dict(message=f"Welcome {patient.first_name}"), status=status.HTTP_200_OK)

            else:
                return Response(
                    dict(invalid_credential='This Email does not exist in our records'),
                    status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(
                dict(invalid_credential='This Email does not exist in our records'),
                status=status.HTTP_400_BAD_REQUEST)


class Calender(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = strip_and_lower(request.data.get('email', ''))

        try:
            doctor = Doctor.objects.get(email = email)
            return Response(dict(message="Yaaaay"))

        except Exception:
            return Response(
                dict(invalid_credential='Sorry, You are not a Doctor.'),
                status=status.HTTP_400_BAD_REQUEST)


