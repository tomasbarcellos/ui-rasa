from django import forms

from .models import AcaoIntencao, Texto, Historia

class HistoriaForm(forms.ModelForm):

    class Meta:
        model = Historia
        fields = ('nome',)
        labels = {
            "nome": "Nome:",
        }   
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control",},
            ),
        }

class AcaoIntencaoForm(forms.ModelForm):

    class Meta:
        model = AcaoIntencao
        fields = ('nome', 'tipo',)
        labels = {
            "nome": "Nome:",
            "tipo": "Ação ou Intenção?",
        }   
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control",},
            ),
            "tipo": forms.Select(
                attrs={"class": "selectpicker form-control"}
            ),
        }

