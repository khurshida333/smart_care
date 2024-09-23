from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import the views module if you have a views.py file

urlpatterns = [
    #  path('', views.home, name='home'),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('doctor/', include('doctor.urls')),  
    path('patient/', include('patient.urls')), 
    path('appointment/', include('appointment.urls')),
    path('service/', include('service.urls')),  
    path('contact_us/', include('contact_us.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
