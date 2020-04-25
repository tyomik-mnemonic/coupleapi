from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, filters, decorators

from .models import OfferTypes, Offer, Form, Status
from .serializers import *

class OfferTypesSet(viewsets.ModelViewSet):
    queryset = OfferTypes.objects.all()
    serializer_class = OfferTypesSerializer
    permission_classes = (permissions.AllowAny,)

class StatusSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (permissions.AllowAny,)

class OfferSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.AllowAny,)

class FormSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (permissions.AllowAny,)