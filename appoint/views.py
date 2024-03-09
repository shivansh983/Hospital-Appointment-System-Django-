# views.py

from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment

def booking(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")  # Extract message field value
        specialization = request.POST.get("specialization")  # Extract specialization field value
        preferred_date = request.POST.get("date")
        preferred_time = request.POST.get("time")
        preferred_doctor = request.POST.get("doctor")

        # Save form data to the Appointment model
        appointment = Appointment.objects.create(
            name=name,
            email=email,
            message=message,
            specialization=specialization,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
            preferred_doctor=preferred_doctor
        )

        return render(request, 'index.html')  # Display a success page
    else:
        return render(request, 'booking.html')

def custom_admin_view(request):
    # Your custom administrative logic here
    return HttpResponse("This is a custom admin page.")
