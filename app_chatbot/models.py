from django.db import models

# historias > intenções + ações
# intenções > textos
# ações > textos

class Historia(models.Model):
    nome = models.CharField(max_length=200)
    ordem = models.PositiveSmallIntegerField("ordem do elemento na história")
    componente = models.ForeignKey(AcaoIntencao)

    def __str__(self):
        return self.nome


class AcaoIntencao(models.Model):
    TIPO_CHOICE = (
        ("Ação", "Ação"),
        ("Intenção", "Intenção"),
    )
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICE,)


    def __str__(self):
        return self.nome


class Texto(models.Model):
    id_acao_intencao = models.ForeignKey(AcaoIntencao)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.nome


