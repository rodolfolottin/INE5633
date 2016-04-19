#coding: utf-8
from Nodo import Nodo
from Heuristica import Heuristica
from Utils import Utils as utils

class EightPuzzleSolver(object):

    _nodo_objetivo = {'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': 8, 'a22': ' '}
    _movimentos_permitidos = ['11', '12', '13', '21', '22',  '23', '31', '32', '33']
    _LINHA = 1
    _COLUNA = 2
    _len_listafronteiras = 0

    def __init__(self):
        self.fronteiras = []
        self.visitados = []

    #Docstring: Função utilizada para descobrir a chave da posição do quadrado vazio
    def _descobrirPecaVazia(self, nodo):
        for chave, valor in nodo.items():
            if valor == ' ':
                return chave, nodo

    def _adicionarNodoListaVisitadosRemoverListaFronteiras(self, nodo):
        self.fronteiras.remove(nodo)
        self.visitados.append(nodo)

    def _retornaProximoFronteira(self):
        return min(self.fronteiras, key=lambda nodo: nodo.heuristicaCaminho())

    def isNodoObjetivo(self, nodo):
        if nodo.estadoTabuleiro == self._nodo_objetivo:
            return True
        return False

    def isNodoJaVisitado(self, nodo):
        for nodoVisitado in self.visitados:
            if nodo.estadoTabuleiro == nodoVisitado.estadoTabuleiro:
                return True
        return False

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

        if self.isNodoJaVisitado(novoNodo) == False:
            novoNodo.pesoHeuristica = self.computarHeuristicas(novoNodo.estadoTabuleiro)
            self.fronteiras.append(novoNodo)

    def computarHeuristicas(self, nodo):
        return Heuristica.distanciaDeManhattan(nodo, self._nodo_objetivo)
        # return Heuristica.distanciaDeManhattan(nodo, self._nodo_objetivo) + Heuristica.numeroDePecasForaDoLugar(nodo, self._nodo_objetivo)

    def AStarAlgorithm(self, nodo, nodoInicial = False):
        if nodoInicial:
            self.fronteiras.append(nodo)
        while self.fronteiras:
            nodoAnalisado = self._retornaProximoFronteira()
            if self.isNodoObjetivo(nodoAnalisado):
                return utils.exibirRelatorio(nodoAnalisado, self._len_listafronteiras)
            self._adicionarNodoListaVisitadosRemoverListaFronteiras(nodoAnalisado)
            for espacoEstado in self.criarEspacosDeEstado(nodoAnalisado.estadoTabuleiro):
                self.configurarNodo(espacoEstado, nodoAnalisado)
            self.analisarExpansaoListaFronteiras()

    def analisarExpansaoListaFronteiras(self):
        self._len_listafronteiras = max(self._len_listafronteiras, len(self.fronteiras))