from rest_framework import viewsets
from apps.clientes.models import Cliente
from apps.clientes.serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer