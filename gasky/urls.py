

from django.contrib import admin
from django.urls import include, re_path, include

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^', include('web.urls',namespace='web')),
]
