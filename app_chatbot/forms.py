from django import forms

from .models import AcaoIntencao, Texto

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
                attrs={"class": "form-control", "rows": "2"},
            ),
            "tipo": forms.Select(
                attrs={"class": "selectpicker form-control"}
            ),
        }

