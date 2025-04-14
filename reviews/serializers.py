from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    patient_email = serializers.EmailField(
        source='patient.email', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'campaign', 'patient',
                  'patient_email', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'patient', 'created_at']
