from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    return render(request,'gerenciar.html')

def cadastrar_banco(request):
    # request.post will receive the values filled in on the form
    # for each named field there is a key in the dictionary
    # to access the fields value use the .get() method with the name of the field
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.POST.get('icone')
    print(request.POST)
    return HttpResponse("Banco cadastrado")
