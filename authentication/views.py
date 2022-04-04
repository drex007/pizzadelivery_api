from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .serializers import UserModelSerializer, UserSerializer,LoginSerializer
from .models import User
from rest_framework.views import APIView
import jwt, datetime


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        data = {
        "message": "Hello this is auth View"
        }
        return Response(data= data)



hello_auth_view = HelloAuthView.as_view()

class UserCreateView(generics.GenericAPIView):
    serializer_class = UserModelSerializer

    def post(self, request):
        data = request.data
        serializer= self.serializer_class(data=data )

        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status = status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

user_creation = UserCreateView.as_view() 




#differnent tutor

# class RegisterView(APIView):

#     def post(self, request):
#         data = request.data
#         serializer  = UserSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


        
# register_user = RegisterView.as_view()

# class LoginView(APIView):
#     serializer_class = LoginSerializer

    
#     @swagger_auto_schema(operation_description="login")
#     def post(self,request):
     
#         data = request.data
#         username = data['username']
#         password = data['password']
#         user = User.objects.filter(email= username).first()
#         if user is None:
#             raise AuthenticationFailed(detail="User Not Found ")
#         if not user.check_password(password):
#             raise AuthenticationFailed(detail="Password is Incorrect")

#         payload = {
#             "id": user.id,
#             "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
#             "iat": datetime.datetime.utcnow()
#         }
#         token = jwt.encode(payload,'secret',algorithm='HS256')

#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt':token 
#         }

#         return response

# login_view = LoginView.as_view()


class GetUser(APIView):
    
   
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed(detail="Unaunthenicated")
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(detail="Expired Signature")
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

getuser = GetUser.as_view()


class LogOut(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "sucess"
        }
        return response

logout_view = LogOut.as_view()
