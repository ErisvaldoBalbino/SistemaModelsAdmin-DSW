from django.contrib import admin
from django.urls import path, include
from core import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('core.urls'))
]
