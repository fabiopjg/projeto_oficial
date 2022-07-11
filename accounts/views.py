from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 

from .forms import UserForm, AlunoForm, EnfermeiroForm, UserEditForm
from .models import CustomUser, Aluno, Enfermeiro

def register(request: HttpRequest):
    if request.POST:
        form = UserForm(request.POST)
    
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)

            if form.cleaned_data['categoria'] == 'aln':
                return redirect('/accounts/register/aluno')
            return redirect('/accounts/register/enfermeiro')
    
    form = UserForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)

@login_required()
def registerAluno(request: HttpRequest):
    if request.POST:
        form = AlunoForm(request.POST)
    
        if form.is_valid():
            form.instance.user = request.user
            form.save()

            return redirect('/')
    
    form = AlunoForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)

@login_required()
def registerEnfermeiro(request: HttpRequest):
    if request.POST:
        form = EnfermeiroForm(request.POST)
    
        if form.is_valid():
            form.instance.user = request.user
            form.save()

            return redirect('/')
    
    form = EnfermeiroForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)

@login_required()
def editar_conta(request):
    try:
        aluno = Aluno.objects.get(user=request.user)

        if request.POST:
            user_form = UserEditForm(request.POST, instance=request.user)
            aluno_form = AlunoForm(request.POST, instance=aluno)

            if user_form.is_valid() and aluno_form.is_valid():
                user_form.save()
                aluno_form.save()
            
                return redirect('/')

        user_form = UserEditForm(instance=request.user)
        aluno_form = AlunoForm(instance=aluno)
        context = {
            'user_form': user_form,
            'form': aluno_form
        }

        return render(request, 'accounts/edit.html', context)
    except:
        enfermeiro = Enfermeiro.objects.get(user=request.user)

        if request.POST:
            user_form = UserEditForm(request.POST, instance=request.user)
            enfermeiro_form = EnfermeiroForm(request.POST, instance=enfermeiro)

            if user_form.is_valid() and enfermeiro_form.is_valid():
                user_form.save()
                enfermeiro_form.save()
                
                return redirect('/')

        user_form = UserEditForm(instance=request.user)
        enfermeiro_form = EnfermeiroForm(instance=enfermeiro)
        context = {
            'user_form': user_form,
            'form': enfermeiro_form
        }

        return render(request, 'accounts/edit.html', context)
        

@login_required()
def listar_alunos(request):
    Enfermeiro.objects.get(user=request.user)

    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos
    }


    return render(request, 'alunos/listar.html', context)

@login_required()
def detail_aluno(request, id_aluno):
    Enfermeiro.objects.get(user=request.user)

    aluno = Aluno.objects.get(pk=id_aluno)
    context = {
        'aluno': aluno
    }

    return render(request, 'alunos/detail.html', context)