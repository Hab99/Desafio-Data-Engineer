from collections import defaultdict
import math

def soma_pares(lista):
    soma = 0
    for l in lista:
        if l%2:
            soma += 0
        else:
            soma +=l
    return soma
    #   return sum(x for x in lista if x % 2 == 0)

def contar_palavra(lista, palavra):
    return lista.count(palavra)

def filtrar_maiores(lista):
    maior = []
    for l in lista:
        if l >10:
            maior.append(l)
    return maior


def agrupar_por_primeira_letra(lista):
    grupos = defaultdict(list)
    for palavra in lista:
        grupos[palavra[0]].append(palavra)
    return grupos

def fatorial(number):
    if number != 0:
        return math.factorial(number)
    else:
        return 1

def converter_data(data):
    return data.split("-")[2] + "/" + data.split("-")[1] + "/" + data.split("-")[0]

def verificar_palindromo(palavra):
    return palavra == palavra[::-1]


def contar_linhas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        contador = 0
        for linha in arquivo.readlines():
            contador += 10
    return contador
