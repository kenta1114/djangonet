from django.contrib import admin
from django.urls import path, include

import djangonet

urlpatterns = [
    path("", include(djangonet.urls)),
    path('admin/', admin.site.urls),
]
