#coding: utf-8
from Nodo import Nodo
from Const import ConstMatriz

import math

class EightPuzzleSolver(object):

    _nodo_objetivo = {'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': 8, 'a22': ' '}
    _movimentos_permitidos = ['11', '12', '13', '21', '22',  '23', '31', '32', '33']
    _LINHA = 1
    _COLUNA = 2

    def __init__(self, nodoInicial):
        self.dicionario = {'Fronteiras': [nodoInicial], 'Visitados': []}

    def __str__(self):
        return ""

    #Docstring: Função utilizada para descobrir a chave da posição do quadrado vazio
    def _descobrirPecaVazia(self, nodo):
        for chave, valor in nodo.items():
            if valor == ' ':
                return chave, nodo

    def descobrirPossibilidadesDeMovimento(self, nodo):
        chave, nodo = self.descobrirPecaVazia(nodo)
        possiveisMovimentos = []

        for x in (-1,1):
            possiveisMovimentos.append(str(int(chave[self._LINHA]) + x) + str(chave[self._COLUNA]))
            possiveisMovimentos.append(str(int(chave[self._LINHA]) + x) + str(chave[self._COLUNA]))
            possiveisMovimentos.append(str(chave[self._LINHA]) + str(int(chave[self._COLUNA]) + x))
            possiveisMovimentos.append(str(chave[self._LINHA]) + str(int(chave[self._COLUNA]) + x))

        possiveisMovimentosIndexados = []
        for movimento in list(set(possiveisMovimentos)):
            if movimento in self._movimentos_permitidos:
                possiveisMovimentosIndexados.append('a' + str(movimento))

        return possiveisMovimentosIndexados, chave

    def criarEspacosDeEstado(self, nodo):
        possiveisMovimentosIndexados, chave = self.descobrirPossibilidadesDeMovimento(nodo)
        novosEspacosDeEstado = []

        for posicao in possiveisMovimentosIndexados:
            nodoTemp = nodo.copy()
            nodoTemp[posicao], nodoTemp[chave] = nodoTemp[chave], nodoTemp[posicao]
            novosEspacosDeEstado.append(nodoTemp)

        return novosEspacosDeEstado

    def isNodoObjetivo(self, nodo):
        return cmp(nodo, self._nodo_objetivo) == 0

    def _gerarChavesDicionario(self):
        chaves = []

        for i in (1,2,3):
            for j in (1,2,3):
                # montando chave de acordo com o index dict
                chaves.append('a' + str(i) + str(j))

        return chaves

    def heuristica_numeroDePecasForaDoLugar(self, nodo):
        numPecasHeuristic = 9

        for chave, valor in nodo.viewitems() & self._nodo_objetivo.viewitems():
            numPecasHeuristic = numPecasHeuristic - 1

        return numPecasHeuristic

    def heuristica_distanciaDeManhattan(self, nodo):
        manhattanHeuristic = 0
        # swap chave e valor dict
        swap_nodo_objetivo = dict((v,k) for k,v in self._nodo_objetivo.iteritems())

        for chave in self._gerarChavesDicionario():
            if nodo[chave] != self._nodo_objetivo[chave]:
                pecaObjtv = swap_nodo_objetivo[nodo[chave]]
                # conversoes pois a chave ('aij') vem como string
                linha = int(chave[self._LINHA])
                coluna = int(chave[self._COLUNA])
                distParaPosicaoCorreta = int(math.fabs(int(pecaObjtv[self._LINHA]) - linha)) +int(math.fabs(int(pecaObjtv[self._COLUNA]) - coluna))
                manhattanHeuristic = manhattanHeuristic + distParaPosicaoCorreta

        return manhattanHeuristic

    # Docstrings: Função utilizada para imprimir um espaço de estado do quebra cabeça de 8 peças
    def exibirEstadoDoNodo(self, nodo):
        j = 1

        for i in (1, 2, 3):
            print('- - - - - - - - - -')
            print('|  ' + str(nodo['a' + str(i) + str(j)]) + '  |  ' + str(nodo['a' + str(i) + str(j + 1)]) + '  |  ' + str(nodo['a' + str(i) + str(j + 2)]) + '  |')
        print('- - - - - - - - - -')


# NODO ERRADO
# N = Nodo({'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a22': ' ', 'a32': 4, 'a31': 6, 'a21': ' '})
# NODO PERFEITO
N = Nodo({'a11': 1, 'a12': 2, 'a13': 3, 'a21': 8, 'a22': 4,'a23': ' ', 'a31': 7, 'a32': 5, 'a33': 6})
C = EightPuzzleSolver(N)
# print C.dicionario['Fronteiras'][0].estadoTabuleiro

print C.exibirEstadoDoNodo(C.dicionario['Fronteiras'][0].estadoTabuleiro)
# C.heuristica_numeroDePecasForaDoLugar(C.dicionario['Fronteiras'][0].estadoTabuleiro)
