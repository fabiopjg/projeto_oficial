from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import DoencaForm
from .models import Doenca
from accounts.models import Enfermeiro

@login_required()
def listar(request):
    doencas = Doenca.objects.all()
    context = {
    'doencas': doencas
    }

    return render(request, 'doencas/listar.html', context)

@login_required()
def criar(request):
    Enfermeiro.objects.get(user=request.user)
    if request.POST:
        form = DoencaForm(request.POST)

        if form.is_valid():
            enfermeiro = Enfermeiro.objects.get(user=request.user)
            form.instance.enfermeiro = enfermeiro
            form.save()

            return redirect('/doencas')
    
    form = DoencaForm()

    context = {
        'form': form,
    }

    return render(request, 'doencas/criar.html', context)

@login_required()
def excluir(request, doenca_id):
    Enfermeiro.objects.get(user=request.user)
    Doenca.objects.get(pk=doenca_id).delete()

    return HttpResponseRedirect("/doencas/") 

@login_required
def editar(request, doenca_id):
    Enfermeiro.objects.get(user=request.user)
    doenca = Doenca.objects.get(pk=doenca_id)

    if request.POST:
        form = DoencaForm(request.POST, instance=doenca)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/doencas")
        
    else:
        form = DoencaForm(instance=doenca)

    context = {
        'form': form,
        'doenca_id': doenca_id
    }

    return render(request, 'doencas/editar.html', context)

@login_required
def detail(request, doenca_id):
    doenca = Doenca.objects.get(pk=doenca_id)
    context = {
        'doenca': doenca
    }
    
    return render(request, 'doencas/detail.html', context)
