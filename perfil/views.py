from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.contrib.messages import constants

from .models import Conta
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def gerenciar(request):
    contas = Conta.objects.all()

    # computing the sum on the client side
    # total_contas = 0
    # f or conta in contas:
    #    total_contas += float(conta.valor)

    # computing the sum on the server side
    total_contas = Conta.objects.aggregate(Sum('valor'))['valor__sum']

    return render(request, 'gerenciar.html', {
        'contas': contas,
        'total_contas': total_contas
    })


def deletar_banco(request, id):
    try:
        Conta.objects.get(pk=id).delete()
        messages.add_message(request, constants.SUCCESS,
                             f"Conta deletada com sucesso.")
    except:
        messages.add_message(request, constants.ERROR,
                             f"Não foi possível deletar a conta {id}.")

    return redirect('/perfil/gerenciar')


def cadastrar_banco(request):
    # request.post will receive the values filled in on the form
    # for each named field there is a key in the dictionary
    # to access the fields value use the .get() method with the name of the field
    apelido = request.POST.get('apelido').strip()
    banco = request.POST.get('banco').strip()
    tipo = request.POST.get('tipo').strip()
    valor = request.POST.get('valor').strip()
    # files use the FILES object to access the files uploaded
    icone = request.FILES.get('icone')

    if len(apelido) == 0:
        print("Não validou")
        messages.add_message(request, constants.ERROR,
                             'Apelido inválido')
        return redirect('/perfil/gerenciar')

    newConta = Conta(apelido=apelido, banco=banco,
                     tipo=tipo, valor=valor, icone=icone)
    newConta.save()

    messages.add_message(request, constants.SUCCESS,
                         f"Conta criada com sucesso. Id={newConta.pk}")

    return redirect('/perfil/gerenciar')
