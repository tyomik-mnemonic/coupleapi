from django.conf import settings
from rest_framework import serializers, utils
from .models import OfferTypes, Offer, Form, Status

class OfferTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfferTypes
        fields = ('id', 'name')


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'name')



class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('id', 'cr_date', 'ch_date', 'str_date', 'stp_date', 'name', 'types', 'min_w', 'max_w', 'fin_user')


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = ('id', 'create_date', 'change_date', 'sname', 'fname', 'tname', 'b_date', 'phone', 'n_doc', 's_we', 'partner')


   


     