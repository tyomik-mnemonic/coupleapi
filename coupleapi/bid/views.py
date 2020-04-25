from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, filters, decorators

from .models import Bid
from .serializers import BidSerializer

class BidSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = (permissions.AllowAny,)


    def get_object(self, pk):
        try:
            return BidSet.objects.get(pk=pk)
        except BidSet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BidSerializer(snippet, many=True)
        return Response(serializer.data)



        