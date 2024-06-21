from rest_framework import serializers
from apps.clientes.models import Cliente
from apps.clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "Número de CPF inválido."})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome": "O nome deve conter apenas letras."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "O RG deve conter 9 dígitos."})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O número do celular deve seguir o padrão: 11 91234-1234."})
        return data