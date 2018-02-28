from django.urls import path, include
from .views import *

urlpatterns = [
	url(r'^/', include('universities.urls')),

]
