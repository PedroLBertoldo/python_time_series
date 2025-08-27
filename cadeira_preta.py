#1-Um cabeçalho não é algo obrigatório da linguagem, mas é uma boa prática.
#Ele é um bloco de comentários (normalmente no início do arquivo) onde o programador coloca informações sobre o código.

"""
Um docstring é uma string especial que serve para documentar módulos, funções, classes ou métodos.
É escrita entre aspas triplas """ """ logo após a definição. 
"""


#O cabeçalho é um bloco de comentários no início do arquivo, usado apenas para dar informações gerais sobre o código, como autor, data e descrição.
#Ele não é interpretado pelo Python.
"""
O docstring é um texto de documentação colocado dentro de funções, classes ou módulos, escrito entre aspas triplas.
Ele pode ser acessado em tempo de execução e usado por ferramentas como help() para explicar o que aquele trecho do código faz.
"""




# formate o cabeçalho deste arquivo após completar os exercícios abaixo:

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    ...

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual
    ...

import re

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...
