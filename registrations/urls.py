from django.urls import path

from . import views
from . import export_views

urlpatterns = [

    path(
        "event/<int:event_id>/",
        views.register_event,
        name="register_event"
    ),

    path(
        "",
        views.registration_list,
        name="registration_list"
    ),

    path(
        "<int:id>/",
        views.registration_detail,
        name="registration_detail"
    ),

    path(
        "cancel/<int:id>/",
        views.cancel_registration,
        name="cancel_registration"
    ),

    path(
        "status/<int:id>/<str:status>/",
        views.update_registration_status,
        name="update_registration_status"
    ),

    path(
        "export/pdf/",
        export_views.export_registration_pdf,
        name="export_registration_pdf"
    ),

    path(
        "export/excel/",
        export_views.export_registration_excel,
        name="export_registration_excel"
    ),

    path(
        "export/excel/",
        views.export_registrations_excel,
        name="export_excel"
    ),

]