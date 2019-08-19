from django.db import models

# historias > intenções + ações
# intenções > textos
# ações > textos

class AcaoIntencao(models.Model):
    TIPO_CHOICE = (
        ("Ação", "Ação"),
        ("Intenção", "Intenção"),
    )
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICE, default="Ação",)

    def __str__(self):
        return self.nome

class Historia(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class PartesHistoria(models.Model):
    historia = models.ForeignKey(Historia, on_delete = models.PROTECT)
    ordem = models.PositiveSmallIntegerField("ordem do elemento na história")
    componente = models.ForeignKey(AcaoIntencao, on_delete = models.PROTECT)

class Texto(models.Model):
    id_acao_intencao = models.ForeignKey(AcaoIntencao, blank=True, on_delete = models.PROTECT)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto


