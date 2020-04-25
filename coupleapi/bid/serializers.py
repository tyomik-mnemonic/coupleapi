from django.conf import settings
from rest_framework import serializers, utils
from .models import Bid

class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = '__all__'
        read_only_fields = ('id', 'cr_date','post_date', 'client','types', 'status')



   


     