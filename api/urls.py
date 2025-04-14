from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    """
    API root endpoint, accessible to all users without authentication.
    """
    return Response({
        'campaigns': reverse('campaign-list', request=request, format=format),
        'reviews': reverse('campaign-reviews', kwargs={'campaign_id': 1}, request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('campaigns.urls')),
    path('', include('bookings.urls')),
    path('', include('reviews.urls')),
    path('', include('users.urls')),
]
