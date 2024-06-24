from rest_framework import viewsets, filters
from apps.clientes.models import Cliente
from apps.clientes.serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClienteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']