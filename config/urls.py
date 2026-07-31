from django.contrib import admin
from django.urls import path, include

from dashboard.views import home, dashboard

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("dashboard/", dashboard, name="dashboard"),

    path("events/", include("events.urls")),

    path( "registrations/", include("registrations.urls")),

]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )