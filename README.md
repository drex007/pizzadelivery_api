# pizzadelivery_api
incase of custom login jwt auth issues



Try this:

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
user = User.objects.first()
refresh = RefreshToken.for_user(user)
raw_token = str(refresh.access_token)
