from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from appoint.views import booking


def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render (request,'about_us.html')

def services(request):
    return render (request,'services.html')

def booking(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        specialization = request.POST.get("specialization")
        preferred_doctor = request.POST.get("preferred_doctor")

        email = EmailMessage(
            subject=f"{name} from Doctor Family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )

        try:
            email.send()
            return HttpResponse("Appointment request sent successfully")
        except:
            return HttpResponse("Failed to send appointment request")

    return render(request, 'booking.html')

def doctor_list(request):
    return render(request, 'Doctors.html')
