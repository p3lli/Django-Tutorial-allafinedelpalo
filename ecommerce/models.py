from __future__ import unicode_literals

import datetime
from django.db import models

class GenericObject(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        abstract = True

class Casa(GenericObject):
    nome = models.CharField(null=False, blank=False, max_length=100)
    about = models.TextField(null=True, blank=True, max_length=400)
    email = models.EmailField(null=False, blank=False,)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return '{} {}'.format(self.nome, self.email)


class Prodotto(GenericObject):

    DIMENSIONI = (('P', 'Piccolo'), ('M', 'Medio'), ('G', 'Grande'),)

    nome = models.CharField(null=False, blank=False, unique=True, max_length=100)
    dettagli = models.TextField(null=True, blank=True, max_length=255)
    prezzo = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    immagine = models.FileField(null=True, blank=True)
    dimensione = models.CharField(null=False, blank=False, max_length=1, choices = DIMENSIONI)
    spedizione_gratuita = models.BooleanField(default=False)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return '{} {}'.format(self.nome, self.prezzo)
