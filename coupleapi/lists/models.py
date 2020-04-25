from django.db import models
from django.contrib.auth.models import User


class OfferTypes(models.Model): # тип предложения
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'тип предложения'
        verbose_name_plural = 'тип предложений'


class Status(models.Model): # статус заявки
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'статус'
        verbose_name_plural = 'статус'


class Offer(models.Model): #предложения
    id = models.BigIntegerField(primary_key=True)
    cr_date = models.DateField(verbose_name='дататайм создания ', editable=False, auto_now_add=True) #а
    ch_date = models.DateField(verbose_name='дататайм изменения', auto_now_add=True) #а
    str_date = models.DateField(verbose_name='дататайм начала ротации')
    stp_date = models.DateField(verbose_name='дататайм окончания ротации')
    name =  models.TextField(null=False)
    types = models.ForeignKey(OfferTypes, models.DO_NOTHING, blank=True, null=True, help_text = 'тип предложения')
    min_w = models.IntegerField('мин  скоринговый балл', blank=True, null=True)
    max_w = models.IntegerField('макс скоринговый балл', blank=True, null=True)
    fin_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, help_text = 'кр_орг')

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'


class Form(models.Model): #анкеты
    id = models.BigIntegerField(primary_key=True)
    create_date = models.DateField(verbose_name='дата и время создания ', editable=False, auto_now_add=True)#а
    change_date = models.DateField(verbose_name='дата и время изменения', auto_now_add=True)#а
    sname = models.TextField(null=False)
    fname = models.TextField(null=False)
    tname = models.TextField(null=False)
    b_date = models.DateField(verbose_name='дата рождения')
    phone = models.CharField('номер телефона',max_length=50, blank=True, null=False)
    n_doc = models.IntegerField('номер паспорта', blank=True, null=True)
    s_we =  models.IntegerField('скоринговый балл', blank=True, null=True)
    partner = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, help_text = 'партнер')


    def __str__(self):
        return self.sname
    def __unicode__(self):
        return self.sname

    class Meta:
        managed = True
        verbose_name = 'анкета'
        verbose_name_plural = 'анкеты'
