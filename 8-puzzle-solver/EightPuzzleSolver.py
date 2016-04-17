#coding: utf-8

from Nodo import Nodo
from Heuristica import Heuristica
from Utils import Utils as utils

class EightPuzzleSolver(object):

    _nodo_objetivo = {'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': 8, 'a22': ' '}
    _movimentos_permitidos = ['11', '12', '13', '21', '22',  '23', '31', '32', '33']
    _LINHA = 1
    _COLUNA = 2

    def __init__(self):
        self.dicionario = {'Fronteiras': [], 'Visitados': []}

    #Docstring: Função utilizada para descobrir a chave da posição do quadrado vazio
    def _descobrirPecaVazia(self, nodo):
        for chave, valor in nodo.items():
            if valor == ' ':
                return chave, nodo

    def _ordenarFronteiras(self):
        self.dicionario['Fronteiras'].sort(key=lambda nodo: nodo.heuristicaCaminho(), reverse=False)

    def _adicionarNodoListaVisitados(self, nodo):
        self.dicionario['Fronteiras'].remove(nodo)
        self.dicionario['Visitados'].append(nodo)

    def _adicionarNodoListaFronteiras(self, nodo):
        self.dicionario['Fronteiras'].append(nodo)

    def _retornaProximoFronteira(self):
        return self.dicionario['Fronteiras'][0]

    def isNodoObjetivo(self, nodo):
        return cmp(nodo, self._nodo_objetivo) == 0

    def isNodoJaVisitado(self, nodo):
        for nodoVisitado in self.dicionario['Visitados']:
            return cmp(nodo.estadoTabuleiro, nodoVisitado.estadoTabuleiro) == 0

    def descobrirPossibilidadesDeMovimento(self, nodo):
        chave, nodo = self._descobrirPecaVazia(nodo)
        possiveisMovimentos = []

        for x in (-1,1):
            possiveisMovimentos.append(str(int(chave[self._LINHA]) + x) + chave[self._COLUNA])
            possiveisMovimentos.append(chave[self._LINHA] + str(int(chave[self._COLUNA]) + x))

        possiveisMovimentosIndexados = []
        for movimento in possiveisMovimentos:
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

    def configurarNodo(self, espacoEstado, nodoAnalisado):
        profundidade = nodoAnalisado.profundidade + 1
        nodoPai = nodoAnalisado

        novoNodo = Nodo(espacoEstado, 0, profundidade, nodoPai)

        if not self.isNodoJaVisitado(novoNodo):
            novoNodo.pesoHeuristica = self.computarHeuristicas(novoNodo.estadoTabuleiro, self._nodo_objetivo)
            self._adicionarNodoListaFronteiras(novoNodo)

    def computarHeuristicas(self, nodo, nodoObjetivo):
        return Heuristica.distanciaDeManhattan(nodo, self._nodo_objetivo) + Heuristica.numeroDePecasForaDoLugar(nodo, self._nodo_objetivo)

    def AStarAlgorithm(self, nodoAnalisado, nodoInicial = False):
        if nodoInicial:
            self.dicionario['Fronteiras'].append(nodoAnalisado)
        if self.isNodoObjetivo(nodoAnalisado.estadoTabuleiro):
            return utils.exibirRelatorio(nodoAnalisado)
        self._adicionarNodoListaVisitados(nodoAnalisado)
        for espacoEstado in self.criarEspacosDeEstado(nodoAnalisado.estadoTabuleiro):
            self.configurarNodo(espacoEstado, nodoAnalisado)
        self._ordenarFronteiras()
        self.AStarAlgorithm(self._retornaProximoFronteira())
