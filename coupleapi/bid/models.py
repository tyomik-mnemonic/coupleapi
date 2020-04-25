from django.db import models
from lists.models import *


class Bid(models.Model): #заявки
    id = models.BigIntegerField(primary_key=True)
    cr_date = models.DateTimeField(verbose_name='дататайм создания ', editable=False, auto_now_add=True) #а
    post_date = models.DateTimeField(verbose_name='дататайм отправки', auto_now_add=True) #а
    client = models.ForeignKey(Form, models.DO_NOTHING, blank=True, null=True, help_text = 'анкета')
    types = models.ForeignKey(OfferTypes, models.DO_NOTHING, blank=True, null=True, help_text = 'тип предложения')
    status = models.ForeignKey(Status, models.DO_NOTHING, blank=True, null=True, help_text = 'статус')
    

    class Meta:
        managed = True
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'


