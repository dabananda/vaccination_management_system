from django.urls import path
from .views import DoctorProfileView, PatientProfileView

urlpatterns = [
    path('doctor/profile/', DoctorProfileView.as_view(), name='doctor-profile'),
    path('patient/profile/', PatientProfileView.as_view(), name='patient-profile'),
]
