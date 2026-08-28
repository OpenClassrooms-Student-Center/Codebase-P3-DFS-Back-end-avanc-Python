from rest_framework import generics

from .models import Equipment
from .serializers import EquipmentSerializer


class EquipmentListView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDetailView(generics.GenericAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def put(self, request, equipment_id, action):
        return self.http_method_not_allowed(request)
