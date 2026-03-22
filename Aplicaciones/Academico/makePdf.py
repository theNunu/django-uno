from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io

def generar_pdf(request, data):
    # Datos para la plantilla
    data = {'nombre': 'Juan Pérez', 'fecha': '2023-10-27'}

    # Renderizar HTML a string
    html_string = render_to_string('pdf_template.html', data)

    # Crear objeto HttpResponse con tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="documento.pdf"'

    # Crear el PDF
    html = io.BytesIO(html_string.encode('utf-8'))
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)

    return response
