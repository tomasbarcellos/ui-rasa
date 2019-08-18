from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms.models import modelformset_factory


# from .models import Historia
from . import forms, models

def historia(request):
    historias = models.Historia.objects.all()
    return render(request, 'app_chatbot/historia.html', {'historias': historias})

def criar_historia(request):
    if request.method == 'POST':
        form = forms.HistoriaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse("criar_historia"))
    else:
        form = forms.HistoriaForm()
    context = {"form": form, }
    return render(request, 'app_chatbot/criar_historia.html', context)

def criar_intencao(request):
    if request.method == 'POST':
        form = forms.AcaoIntencaoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse("criar_intencao"))
    else:
        form = forms.AcaoIntencaoForm()
    context = {"form": form, }
    return render(request, 'app_chatbot/criar_intencao.html', context)

def criar_acao(request):
    if request.method == 'POST':
        form = forms.AcaoIntencaoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse("criar_acao"))
    else:
        form = forms.AcaoIntencaoForm()
    context = {"form": form, }
    return render(request, 'app_chatbot/criar_acao.html', context)

def criar_texto(request):
    if request.method == 'POST':
        form = forms.TextoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse("criar_texto"))
    else:
        form = forms.TextoForm()
    context = {"form": form, }
    return render(request, 'app_chatbot/criar_texto.html', context)
