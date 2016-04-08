#coding: utf-8
from node import Nodo
from const import ConstMatriz

class EightPuzzleSolver(object):

    #TICKET 4: variaveis globais python? como utilizá-las?
    _estado_objetivo = {'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': 8, 'a22': ' '}

    #feio p caralho
    LINHA = 1
    COLUNA = 2

    def __init__(self, nodoInicial):
        self.dicionario = {'Fronteiras': [nodoInicial], 'Visitados': []}

    def __str__(self):
        return ""

    #Docstring: Função utilizada para descobrir a chave da posição do quadrado vazio
    def descobrirPecaVazia(self, nodo):
        for chave, valor in nodo.items():
            if valor == ' ':
                return chave, nodo

    def descobrePossibilidadesDeMovimento(self, nodo):
        pass

    def criarEspacosDeEstado(self, nodo, chave):
        troca_posicoes = self.descobrePossibilidadesDeMovimento(nodo)
        novosEspacosDeEstado = []

        # colocar na classe talvez? passagem parametro?
        chave = 'a11'

        for posicao in troca_posicoes:
            nodoTemp = nodo.copy()
            nodoTemp[posicao], nodoTemp[chave] = nodoTemp[chave], nodoTemp[posicao]
            novosEspacosDeEstado.append(nodoTemp)

        print novosEspacosDeEstado

    def isNodoObjetivo(self, nodo):
        return True if cmp(nodo, self._estado_objetivo) == 0 else False


# NODO ERRADO
# N = Nodo({'a11': ' ', 'a12': 5, 'a13': 4, 'a21': 1, 'a22': 10, 'a23': 8, 'a31': 1, 'a32': 3, 'a33': 6})

# NODO COM TUPLAS
# N = Nodo({(1,1): 3, (1,2): 5, (1,3): 4, (2,1): 1, (2,2): ' ', (2,3): 8, (3,1): 1, (3,2): 3, (3,3): 6})

# NODO PERFEITO
N = Nodo({'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': 8, 'a22': ' '})

# print C.dicionario['Fronteiras'][0].estadoTabuleiro.get('a12')
C.isNodoObjetivo(C.dicionario['Fronteiras'][0].estadoTabuleiro)