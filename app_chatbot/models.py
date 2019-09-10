from django.db import models

# historias > partes
# partes = intenções | ações
# intenções | ações > textos

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
    historia = models.ForeignKey(Historia, blank=True, on_delete = models.CASCADE)
    ordem = models.PositiveSmallIntegerField("ordem do elemento na história", blank=True)
    componente = models.ForeignKey(AcaoIntencao, on_delete = models.PROTECT)

    def __str__(self):
        return str(self.historia) + ": " + str(self.ordem) + " - " + str(self.componente)

class Texto(models.Model):
    id_acao_intencao = models.ForeignKey(AcaoIntencao, blank=True, on_delete = models.CASCADE)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto


