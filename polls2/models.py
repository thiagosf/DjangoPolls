# -*- coding: utf-8 -*-

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
    question = models.CharField("Questão", max_length=200)
    pub_date = models.DateTimeField("Data de publicação")

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publicado recentemente?'

    class Meta:
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField("Texto da opção", max_length=200)
    votes = models.IntegerField("Votos", default=0)

    def __unicode__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"
