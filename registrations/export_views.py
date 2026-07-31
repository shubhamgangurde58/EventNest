from django.http import HttpResponse

from openpyxl import Workbook

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from .models import Registration


def export_registration_excel(request):

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Registrations"

    sheet.append([
        "ID",
        "Student",
        "Email",
        "Phone",
        "College",
        "Department",
        "Year",
        "Event",
        "Status",
        "Registration Date"
    ])

    registrations = Registration.objects.select_related("event")

    for registration in registrations:

        sheet.append([

            registration.id,

            registration.full_name,

            registration.email,

            registration.phone,

            registration.college,

            registration.department,

            registration.year,

            registration.event.title,

            registration.status,

            registration.registration_date.strftime(
                "%d-%m-%Y %H:%M"
            )

        ])

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (
        'attachment; filename="registrations.xlsx"'
    )

    workbook.save(response)

    return response



def export_registration_pdf(request):

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        'attachment; filename="registrations.pdf"'
    )

    pdf = SimpleDocTemplate(
        response,
        pagesize=A4
    )

    data = [[

        "ID",

        "Student",

        "Event",

        "Status"

    ]]

    registrations = Registration.objects.select_related("event")

    for registration in registrations:

        data.append([

            registration.id,

            registration.full_name,

            registration.event.title,

            registration.status

        ])

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.beige),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

        ])

    )

    pdf.build([table])

    return response