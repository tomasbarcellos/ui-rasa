from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Historia
from . import forms

def historia(request):
    historias = Historia.objects.all()
    return render(request, 'app_chatbot/historia.html', {'historias': historias})

def criar_intencao(request):
    if request.method == 'POST':
        form = forms.AcaoIntencaoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse("intencao"))
    else:
        form = forms.AcaoIntencaoForm()
    context = {"form": form, }
    return render(request, 'app_chatbot/criar_intencao.html', context)

