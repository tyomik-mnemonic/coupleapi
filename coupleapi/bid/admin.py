from django.contrib import admin
from dynamic_raw_id.admin import *
from .models import Bid

@admin.register(Bid)
class BidAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_filter = ('id', 'cr_date')
    search_fields = ('id', 'cr_date', 'client')
    list_display = ('id', 'cr_date', 'post_date', 'client', 'types', 'status')

