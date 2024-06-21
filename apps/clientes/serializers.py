from rest_framework import serializers
from apps.clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve conter 11 dígitos.")
        return cpf

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome deve conter apenas letras.")
        return nome
