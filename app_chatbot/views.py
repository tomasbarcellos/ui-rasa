from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms.models import modelformset_factory


from . import forms, models

def listar_historia(request):
    textos = models.Texto.objects.all()
    return render(request, 'app_chatbot/historia.html', {'textos': textos})

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

def criar_acao_intencao(request, tipo):
    N_EXTRA = 10
    TextoFormset = modelformset_factory(
        models.Texto, form=forms.TextoForm, extra=N_EXTRA, min_num=1,
    )
    if tipo == "acao":
        tipo_txt = "Ação"
    else:
        tipo_txt = "Intenção"

    queryset = models.Texto.objects.none()
    formset = TextoFormset(request.POST or None, queryset=queryset)
    form = forms.AcaoIntencaoForm(request.POST or None)
    if form.is_valid() and formset.is_valid():
        instance = form.save(commit=False)
        instance.save()
        saved_id = instance.pk
        instances = formset.save(commit=False)
        for insta in instances:
            insta.id_acao_intencao_id = saved_id
            insta.save()
        return redirect(reverse("criar_acao_intencao", kwargs={"tipo": tipo}))
    context = {
        "form": form,
        "formset": formset,
        "tipo": tipo_txt,
    }
    return render(request, 'app_chatbot/criar_acao_intencao.html', context)

# 2. Criar view em que há uma lista de todas as intenções
# deve listar os X primeiros (uma uma amostra de tamanho X) exemplos
def listar_acoesintencoes(request, tipo):
    # ta errado mas a logica é essa
    if tipo == "acao":
        tipo_txt = "Ação"
    else:
        tipo_txt = "Intenção"

    acao_intencao = models.AcaoIntencao.objects.all().filter(tipo = tipo_txt)
    textos = models.Texto.objects.all()
    
    context = {
        "pais": acao_intencao,
        "textos": textos,
    }
    return render(request, 'app_chatbot/listar_acoesintencoes.html', context)

