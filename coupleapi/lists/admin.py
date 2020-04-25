from django.contrib import admin
from dynamic_raw_id.admin import *
from .models import OfferTypes, Offer, Form, Status
# Register your models here.
@admin.register(OfferTypes)
class OfferTypesAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    list_display = ('id', 'name')

@admin.register(Status)
class StatusAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    list_display = ('id', 'name')

@admin.register(Offer)
class OfferAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_filter = ('id', 'types')
    search_fields = ('id', 'name', 'types')
    list_display = ('id', 'cr_date', 'ch_date', 'str_date', 'stp_date', 'name', 'types', 'min_w', 'max_w', 'fin_user')


@admin.register(Form)
class FormAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_filter = ('id', 'create_date')
    search_fields = ('id', 'create_date', 'change_date', 'sname', 'fname', 'tname', 'b_date', 'phone', 'n_doc', 's_we', 'partner')
    list_display = ('id', 'create_date', 'change_date', 'sname', 'fname', 'tname', 'b_date', 'phone', 'n_doc', 's_we', 'partner')

# Register your models here.


