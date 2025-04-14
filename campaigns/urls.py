from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('campaigns', CampaignViewSet, basename='campaign')

urlpatterns = [
    path('', include(router.urls)),
]
