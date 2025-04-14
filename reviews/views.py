from rest_framework import generics, serializers
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsReviewAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from campaigns.models import Campaign


class CampaignReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(campaign_id=self.kwargs['campaign_id'])

    def perform_create(self, serializer):
        campaign = Campaign.objects.get(id=self.kwargs['campaign_id'])
        user = self.request.user

        from bookings.models import Booking
        if not Booking.objects.filter(patient=user, campaign=campaign).exists():
            raise serializers.ValidationError(
                "You must book this campaign to leave a review.")

        serializer.save(patient=user, campaign=campaign)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]
