
from django.contrib import admin
from django.urls import path
from .views import hello_auth_view, user_creation, login_view,getuser,logout_view
# register_user,
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/',hello_auth_view, name="hello-auth"),
    path('auth/signup/',user_creation, name="signup"),
    # path('auth/register/',register_user, name="register"),
    # path('auth/login/',login_view, name="login"),
    path('auth/getUser/',getuser, name="get-user"),
    path('auth/logout/',logout_view, name="login"),


]
