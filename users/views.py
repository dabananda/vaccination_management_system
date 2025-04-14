from rest_framework import generics, permissions
from .serializers import UserProfileSerializer
from .permissions import IsDoctor, IsPatient


class DoctorProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile


class PatientProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsPatient]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile
