from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    campaign_title = serializers.CharField(
        source='campaign.title', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'campaign', 'campaign_title',
                  'dose_1_date', 'dose_2_date']
        read_only_fields = ['dose_2_date']
