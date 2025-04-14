from django.urls import path
from .views import CampaignReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('campaigns/<int:campaign_id>/reviews/',
         CampaignReviewListCreateView.as_view(), name='campaign-reviews'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
