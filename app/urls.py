from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	url(r'^universities/', include('universities.urls')),
	
	#developer Tools
    path('admin/', admin.site.urls),

]
