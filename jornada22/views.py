from django.http import HttpResponse, request, FileResponse
from django.shortcuts import redirect, render
from .models import Evento, Banner, Organizador,Programacao, Inscrito, Palestrante

from django.contrib import messages
from django.contrib.messages import constants

#pdf
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

# Create your views here.

def index(request):
    evento = Evento.objects.all()[:1]
    banner = Banner.objects.all()[:1]
    organizador = Organizador.objects.all()[:1]
    programacao = Programacao.objects.all()
    palestrantes = Palestrante.objects.all()
    return render(request,'index.html', {'evento': evento, 'banner': banner, 'organizador': organizador, 'programacao': programacao, 'palestrantes': palestrantes})


def add_inscrito(request):    
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        try:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            cpf = request.POST.get('cpf')
            Inscrito.objects.create(nome=nome, email=email, cpf=cpf)
            messages.success (request, 'INSCRIÇÃO REALIZADA COM SUCESSO !')
            Inscrito()

        except:
            messages.error (request, 'CPF JÁ EXISTE !')
            return redirect('/')

    return redirect('/')


def generate_pdf(request):
    # criar Bytestream buffer
    documentTitle = 'exemplo'
    t = 'titulo'
    titulo = 'Lista de Presença'

    textLines = [
        'TESTE DE ARQUIVOS PDF'
    ]
    buf = io.BytesIO()
    # Crie a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0) #Canvas é pra desenhar coisas no pdf
    c.setTitle(documentTitle) #nome do documento
    c.setFont("Courier-Bold", 36) # tipo e tamanho da font
    c.drawCentredString(300,50, titulo) # titulo do pdf
    c.setFillColorRGB(0, 0, 255) # cor das lista
    # drawing a line - uma linha reta
    c.line(30, 70, 550,70) #x1,y1,x2,y2
    # creating a multiline text using
    # textline and for loop
    text = c.beginText(40, 680)
    text.setFont("Courier", 12)
    text.setFillColor(colors.blue) # cor da lista

    for line in textLines:
        text.textLine(line)

    c.drawText(text)

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    #addcione a model para incluir no pdf
    insc = Inscrito.objects.all()
    lines =[]
    for i in insc:
        lines.append(i.nome)
    # loop
    for line in lines:
       textob.textLine()
       textob.textLine('Inscrito: ' + line)

    # finish
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='elionai.pdf')


    


