from django.contrib import admin
from django.urls import path, include
from appoint import views as appoint_views  
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('booking/', appoint_views.booking, name='booking'),
    path('Doctors/', views.doctor_list, name='doctors'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
