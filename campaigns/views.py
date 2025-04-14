from rest_framework import viewsets
from .models import Campaign
from .serializers import CampaignSerializer
from .permissions import IsDoctorOrReadOnly
from rest_framework.permissions import AllowAny


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsDoctorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()
