# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    cpf_cnpj = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Proposta(models.Model):

    #__Proposta_FIELDS__
    id_proposta = models.IntegerField(null=True, blank=True)
    data_criacao_prosposta = models.DateTimeField(blank=True, null=True, default=timezone.now)
    titulo_proposta = models.TextField(max_length=255, null=True, blank=True)
    data_viagem = models.DateTimeField(blank=True, null=True, default=timezone.now)
    id_status_proposta = models.ForeignKey(STATUS_PROPOSTA, on_delete=models.CASCADE)
    capa = models.TextField(max_length=255, null=True, blank=True)

    #__Proposta_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta")
        verbose_name_plural = _("Proposta")


class Status_Proposta(models.Model):

    #__Status_Proposta_FIELDS__
    id_status_proposta = models.TextField(max_length=255, null=True, blank=True)
    status_proposta = models.TextField(max_length=255, null=True, blank=True)

    #__Status_Proposta_FIELDS__END

    class Meta:
        verbose_name        = _("Status_Proposta")
        verbose_name_plural = _("Status_Proposta")


class Proposta_Passageiro(models.Model):

    #__Proposta_Passageiro_FIELDS__
    id_proposta_passageiro = models.IntegerField(null=True, blank=True)
    id_proposta = models.ForeignKey(PROPOSTA, on_delete=models.CASCADE)
    nome_passageiro = models.TextField(max_length=255, null=True, blank=True)

    #__Proposta_Passageiro_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta_Passageiro")
        verbose_name_plural = _("Proposta_Passageiro")


class Proposta_Destino_Fotos(models.Model):

    #__Proposta_Destino_Fotos_FIELDS__
    id_proposta_destino_fotos = models.IntegerField(null=True, blank=True)
    foto = models.TextField(max_length=255, null=True, blank=True)
    id_proposta_destino = models.ForeignKey(PROPOSTA_DESTINO, on_delete=models.CASCADE)

    #__Proposta_Destino_Fotos_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta_Destino_Fotos")
        verbose_name_plural = _("Proposta_Destino_Fotos")


class Proposta_Destino(models.Model):

    #__Proposta_Destino_FIELDS__
    id_proposta = models.ForeignKey(PROPOSTA, on_delete=models.CASCADE)
    titulo_destino = models.TextField(max_length=255, null=True, blank=True)
    data_chegada = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data_saida = models.DateTimeField(blank=True, null=True, default=timezone.now)
    descricao_destino = models.TextField(max_length=255, null=True, blank=True)
    img_destino = models.TextField(max_length=255, null=True, blank=True)
    data_criacao = models.DateTimeField(blank=True, null=True, default=timezone.now)
    localizacao = models.TextField(max_length=255, null=True, blank=True)

    #__Proposta_Destino_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta_Destino")
        verbose_name_plural = _("Proposta_Destino")


class Proposta_Passagem_Transporte(models.Model):

    #__Proposta_Passagem_Transporte_FIELDS__
    id_proposta_destino_transporte = models.IntegerField(null=True, blank=True)
    id_proposta_destino = models.ForeignKey(PROPOSTA_DESTINO, on_delete=models.CASCADE)
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    origem = models.TextField(max_length=255, null=True, blank=True)
    destino = models.TextField(max_length=255, null=True, blank=True)
    embarque = models.DateTimeField(blank=True, null=True, default=timezone.now)
    voo = models.TextField(max_length=255, null=True, blank=True)
    cia_aerea = models.TextField(max_length=255, null=True, blank=True)

    #__Proposta_Passagem_Transporte_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta_Passagem_Transporte")
        verbose_name_plural = _("Proposta_Passagem_Transporte")


class Data(models.Model):

    #__Data_FIELDS__
    id_data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Data_FIELDS__END

    class Meta:
        verbose_name        = _("Data")
        verbose_name_plural = _("Data")


class Day_Bay_Day(models.Model):

    #__Day_Bay_Day_FIELDS__
    id_data = models.ForeignKey(DATA, on_delete=models.CASCADE)
    inicio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fim = models.DateTimeField(blank=True, null=True, default=timezone.now)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    id_proposta_destino = models.ForeignKey(PROPOSTA_DESTINO, on_delete=models.CASCADE)
    foto = models.TextField(max_length=255, null=True, blank=True)

    #__Day_Bay_Day_FIELDS__END

    class Meta:
        verbose_name        = _("Day_Bay_Day")
        verbose_name_plural = _("Day_Bay_Day")


class Proposta_Destino_Hospedagem(models.Model):

    #__Proposta_Destino_Hospedagem_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    localizacao = models.TextField(max_length=255, null=True, blank=True)
    endereco = models.TextField(max_length=255, null=True, blank=True)
    checkin = models.DateTimeField(blank=True, null=True, default=timezone.now)
    checkout = models.DateTimeField(blank=True, null=True, default=timezone.now)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    id_proposta_destino = models.ForeignKey(PROPOSTA_DESTINO, on_delete=models.CASCADE)
    id_proposta_destino_hosédagem = models.IntegerField(null=True, blank=True)

    #__Proposta_Destino_Hospedagem_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta_Destino_Hospedagem")
        verbose_name_plural = _("Proposta_Destino_Hospedagem")


class Proposta_Destino_Hospedagem_Opcao(models.Model):

    #__Proposta_Destino_Hospedagem_Opcao_FIELDS__
    id_proposta_destino_hospedagem_opcao = models.ForeignKey(PROPOSTA_DESTINO_HOSPEDAGEM, on_delete=models.CASCADE)
    opcoes = models.TextField(max_length=255, null=True, blank=True)
    id_proposta_destino_hospedagem = models.ForeignKey(PROPOSTA_DESTINO_HOSPEDAGEM, on_delete=models.CASCADE)

    #__Proposta_Destino_Hospedagem_Opcao_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta_Destino_Hospedagem_Opcao")
        verbose_name_plural = _("Proposta_Destino_Hospedagem_Opcao")


class Proposta_Destino_Hospedagem_Opcao_Fotos(models.Model):

    #__Proposta_Destino_Hospedagem_Opcao_Fotos_FIELDS__
    foto = models.TextField(max_length=255, null=True, blank=True)
    id_proposta_destino_hospedagem_opcao = models.ForeignKey(PROPOSTA_DESTINO_HOSPEDAGEM, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=255, null=True, blank=True)

    #__Proposta_Destino_Hospedagem_Opcao_Fotos_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta_Destino_Hospedagem_Opcao_Fotos")
        verbose_name_plural = _("Proposta_Destino_Hospedagem_Opcao_Fotos")



#__MODELS__END
