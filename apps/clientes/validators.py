import re

def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11

def nome_valido(self, nome):
    return nome.isalpha()

def rg_valido(self, rg):
    return len(rg) == 9

def celular_valido(self, celular):
    """Verifica se o celular é válido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta