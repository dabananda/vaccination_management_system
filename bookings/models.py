from datetime import timedelta
from django.db import models
from users.models import User
from campaigns.models import Campaign


class Booking(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name='bookings')
    dose_1_date = models.DateField()
    dose_2_date = models.DateField(blank=True)

    class Meta:
        unique_together = ('patient', 'campaign')

    def save(self, *args, **kwargs):
        if not self.dose_2_date:
            self.dose_2_date = self.dose_1_date + timedelta(days=28)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient.email} booked {self.campaign.title}"
