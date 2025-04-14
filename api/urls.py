from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campaigns.views import CampaignViewSet
from bookings.views import BookingViewSet

router = DefaultRouter()
router.register('campaigns', CampaignViewSet, basename='campaign')
router.register('bookings', BookingViewSet, basename='booking')

schema_view = get_schema_view(
    openapi.Info(
        title="Vaccination Management API",
        default_version='v1',
        description="API for managing vaccine campaigns, bookings, and users",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('users.urls')),
    path('', include('reviews.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
