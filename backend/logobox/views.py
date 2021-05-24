from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LogoBox

from .serializers import LogoBoxSerializer
import random


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        logos = LogoBox.objects.all()
        serializer = LogoBoxSerializer(logos, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LogoBoxSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        logos = LogoBox.objects.get(id=pk)
        serializer = LogoBoxSerializer(logos)
        return Response(serializer.data)

    def update(self, request, pk=None):
        logos = LogoBox.objects.get(id=pk)
        serializer = LogoBoxSerializer(instance=logos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        logos = LogoBox.objects.get(id=pk)
        logos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
