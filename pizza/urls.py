from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#drf-yasg files stops here
from django.contrib import admin
from django.urls import path, include
from authentication import urls
from orders import urls

#You can use these views or you use djsoers to give you access to more url jwt urls 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

schema_view = get_schema_view(
   openapi.Info(
      title="PIZZA DEVLIVERY API",
      default_version='v1',
      description="Just a pizza Apis and Endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="viktor@gmail.com"),
   
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('orders.urls')),
   #  path('auth/', include('djoser.urls.jwt')), # Gave us the priviledge to use jwt urls 
    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]