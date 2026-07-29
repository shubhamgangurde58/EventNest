from django.urls import path
from . import views

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
    

]