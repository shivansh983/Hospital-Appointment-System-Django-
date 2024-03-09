from django.contrib import admin
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Appointment
from django.conf import settings

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'specialization', 'preferred_date', 'preferred_time', 'preferred_doctor')
    list_filter = ('preferred_date', 'preferred_time', 'preferred_doctor')
    search_fields = ('name', 'email', 'preferred_doctor')

    def send_mail_action(self, request, queryset):
        for appointment in queryset:
            subject = 'Appointment Confirmation'
            message = f'Your appointment with {appointment.preferred_doctor} is scheduled for {appointment.preferred_date} at {appointment.preferred_time}.'
            recipient = appointment.email

            # Send email
            send_mail(subject, message, 'hospitalbooking496@gmail.com', [recipient], fail_silently=False)
        
        self.message_user(request, f"{len(queryset)} email(s) sent successfully.")

    send_mail_action.short_description = "Send Mail"

    # Register custom action
    actions = [send_mail_action]

admin.site.register(Appointment, AppointmentAdmin)
