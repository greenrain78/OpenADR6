from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import equipments_info
from .serializers import EquipmentsInfoSerializer


class EquipmentsInfoViewSet(ModelViewSet):
    queryset = equipments_info.objects.all()
    serializer_class = EquipmentsInfoSerializer
    permission_classes = [AllowAny]
