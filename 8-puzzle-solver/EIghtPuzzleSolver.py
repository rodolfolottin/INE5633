#coding: utf-8
from Nodo import Nodo
from Const import ConstMatriz

class EightPuzzleSolver(object):

    _nodo_objetivo = {'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': 8, 'a22': ' '}
    _movimentos_permitidos = ['11', '12', '13', '23', '33', '32', '31', '21', '22']
    _LINHA = 1
    _COLUNA = 2

    def __init__(self, nodoInicial):
        self.dicionario = {'Fronteiras': [nodoInicial], 'Visitados': []}

    def __str__(self):
        return ""

    #Docstring: Função utilizada para descobrir a chave da posição do quadrado vazio
    def descobrirPecaVazia(self, nodo):
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
        return cmp(nodo, self._estado_objetivo) == 0

    def heuristica_numeroDePecasForaDoLugar(self, nodo):
        numPecas = 9

        for key, value in nodo.viewitems() & self._nodo_objetivo.viewitems():
            numPecas = numPecas - 1

        print numPecas

    def algoritmoAEstrela(self):
        pass

# NODO ERRADO
N = Nodo({'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a22': ' ', 'a32': 4, 'a31': 6, 'a21': ' '})

# NODO COM TUPLAS
# N = Nodo({(1,1): 3, (1,2): 5, (1,3): 4, (2,1): 1, (2,2): ' ', (2,3): 8, (3,1): 1, (3,2): 3, (3,3): 6})

# NODO PERFEITO
# N = Nodo({'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': 8, 'a22': ' '})
C = EightPuzzleSolver(N)
# print C.dicionario['Fronteiras'][0].estadoTabuleiro

print C.isNodoObjetivo(C.dicionario['Fronteiras'][0].estadoTabuleiro)
C.heuristica_numeroDePecasForaDoLugar(C.dicionario['Fronteiras'][0].estadoTabuleiro)
