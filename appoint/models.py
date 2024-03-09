from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()  # Added field
    specialization = models.CharField(max_length=100)  # Added field
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    preferred_doctor = models.CharField(max_length=100)

    class Meta:
        app_label = 'appoint'

    def __str__(self):
        return f'{self.name} - {self.preferred_date} {self.preferred_time} {self.message} {self.specialization}'
