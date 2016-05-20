# coding: utf-8
import copy
import time
from random import randint
from Utils import Utils
from Peca import Peca
from Nodo import Nodo
from Heuristica import Heuristica


class Minimax(object):

    def __init__(self, tab, lenTab, profundidade):
        self._tab = tab
        self._lenTab = lenTab
        self._heuristc = Heuristica()
        self._profundidade = profundidade
        self._nodos = list()

    def expandeNodos(self, nodo, indice, profundidade):
        if not nodo._beta < nodo._alpha:
            self._nodos.append(self.criarNodoFilho(nodo, indice, profundidade + 1))
            filho = self._nodos[-1]
            filho._heuristica = self._heuristc.computarHeuristicaTabuleiro(filho, self.gerarIndicesPossiveisDeJogadaOtimiz(filho._board))

            if not (filho._isNodoFolha or filho._profundidade == self._profundidade):
                for ind in self.gerarIndicesPossiveisDeJogadaOtimiz(filho._board):
                    self.expandeNodos(filho, ind, filho._profundidade)

            self.podaMinimax(nodo, filho)

    def callMinimax(self, nodo, profundidade):
        self._nodos = list()
        self._nodos.append(nodo)

        for indice in self.gerarIndicesPossiveisDeJogadaOtimiz(nodo._board):
            self.expandeNodos(nodo, indice, profundidade)

        # retorna melhor solucao que subiu para primeiro nivel
        listaretornados = []
        for nodo in self._nodos:
            if nodo._profundidade == 1:
                listaretornados.append(nodo)

        return max(listaretornados, key=lambda nodo: nodo._heuristica)

    def podaMinimax(self, pai, filho):
        if (filho._profundidade % 2) == 0:
            if filho._heuristica < pai._beta:
                pai._heuristica = filho._heuristica
            pai._beta = pai._heuristica
        else:
            if filho._heuristica > pai._alpha:
                pai._heuristica = filho._heuristica
            pai._alpha = pai._heuristica

    def gerarIndicesPossiveisDeJogada(self, tab):
        indicesPossiveis = []
        colunasIrrelv = []

        for linha in xrange(self._lenTab - 1, - 1, - 1):
            for coluna in xrange(len(self._tab[linha])):
                if coluna not in colunasIrrelv:
                    if tab[linha][coluna] == Peca.VAZIA:
                        colunasIrrelv.append(coluna)
                        indicesPossiveis.append(int(str(linha) + str(coluna)))

        return indicesPossiveis

    def gerarIndicesPossiveisDeJogadaOtimiz(self, tab):
        indicesPossiveis = []
        colunasIrrelv = []

        for coluna in (3, 2, 4, 1, 5, 0, 6):
            for linha in xrange(self._lenTab - 1, - 1, - 1):
                if coluna not in colunasIrrelv:
                    if tab[linha][coluna] == Peca.VAZIA:
                        colunasIrrelv.append(coluna)
                        indicesPossiveis.append(int(str(linha) + str(coluna)))

        return indicesPossiveis

    def criarNodoFilho(self, nodo, indice, profundidade):
        linha, coluna = Utils.parserJogada(str(indice))
        index = int(str(linha) + str(coluna))

        if (profundidade % 2) != 0:
            pecaJogada = Peca.COMPUTADOR
        else:
            pecaJogada = Peca.JOGADOR

        tabuleiro = copy.deepcopy(nodo._board)
        tabuleiro[linha][coluna] = pecaJogada

        isNodoFolha = self.analisaAdjacenciasPecaJogada(tabuleiro, linha, coluna, pecaJogada)
        return Nodo(index, tabuleiro, pecaJogada, None, profundidade, isNodoFolha, -9999999999, 9999999999)

    def analisaAdjacenciasPecaJogada(self, tab, linha, coluna, pecaJogada):
        if self.analisaColunaPecaJogada(tab, linha, coluna, pecaJogada) or \
                self.analisaLinhaPecaJogada(tab, linha, pecaJogada) or self.analisaDiagonaisPecaJogada(tab, linha, coluna, pecaJogada):
            return True

    def analisaColunaPecaJogada(self, tab, linha, coluna, pecaJogada):
        sequencia = 1

        # descendo coluna, verificações em linha reta
        for valorLinha in xrange(linha + 1, self._lenTab, 1):
            if tab[valorLinha][coluna] == pecaJogada:
                sequencia += 1
                if sequencia == 4:
                    break
            else:
                sequencia = 0
        return sequencia == 4

    def analisaLinhaPecaJogada(self, tab, linha, pecaJogada):
        sequencia = 0

        for indiceColuna in xrange(7):
            if tab[linha][indiceColuna] == pecaJogada:
                sequencia += 1
                if sequencia == 4:
                    break
            else:
                sequencia = 0

        return sequencia == 4

    def analisaDiagonaisPecaJogada(self, tab, linha, coluna, pecaJogada):
        return self._analisaEsqInf(tab, linha, coluna, pecaJogada) or self._analisaDirInf(tab, linha, coluna, pecaJogada)

    def _analisaEsqInf(self, tab, linha, coluna, pecaJogada):
        # print 'Linha e coluna analisadas:', linha, coluna
        limiteBoard = False
        indLinha = linha
        indColuna = coluna
        sequencia = 0

        # estrategia para descer ao ponto mais a esquerda e baixo da diagonal e começar a percorrer dali
        while not limiteBoard:
            # descobrir indices do tab que nao importam e colocar aqui
            # print 'Percorrendo caminho', indLinha, indColuna
            if max(5, indLinha + 1) == 5 and min(0, indColuna - 1) == 0:
                indLinha += 1
                indColuna -= 1
            else:
                break

        # print 'O que ele manda como ponta', indLinha, indColuna
        for x in range(0, 6):
            # print 'Percorrendo e analisando', indLinha, indColuna
            if tab[indLinha][indColuna] == pecaJogada:
                sequencia += 1
            else:
                sequencia = 0

            if sequencia == 4:
                break
            indLinha -= 1
            indColuna += 1
            # print 'Valor que adquirem na iteração de análise', indLinha, indColuna
            if indLinha < 0 or indColuna > 6:
                return False

        return sequencia == 4

    def _analisaDirInf(self, tab, linha, coluna, pecaJogada):
        # print 'Linha e coluna analisadas:', linha, coluna
        limiteBoard = False
        indLinha = linha
        indColuna = coluna
        sequencia = 0

        # estrategia para descer ao ponto mais a direita e baixo da diagonal e começar a percorrer dali
        while not limiteBoard:
            # descobrir indices do tab que nao importam e colocar aqui
            # print 'Percorrendo caminho', indLinha, indColuna
            if max(5, indLinha + 1) == 5 and max(6, indColuna + 1) == 6:
                indLinha += 1
                indColuna += 1
            else:
                break

        # print 'O que ele manda como ponta', indLinha, indColuna
        for x in range(0, 6):
            # print 'Percorrendo e analisando', indLinha, indColuna
            if tab[indLinha][indColuna] == pecaJogada:
                sequencia += 1
            else:
                sequencia = 0

            if sequencia == 4:
                break
            indLinha -= 1
            indColuna -= 1
            # print 'Valor que adquirem na iteração de análise', indLinha, indColuna
            if indLinha < 0 or indColuna < 0:
                return False

        return sequencia == 4
