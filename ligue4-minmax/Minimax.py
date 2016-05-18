# coding: utf-8
import copy
from Utils import Utils
from Peca import Peca
from Nodo import Nodo
from Heuristica import Heuristica


class Minimax(object):

    def __init__(self, tab, lenTab):
        self._tab = tab
        self._lenTab = lenTab
        self._heuristc = Heuristica()

    def alphabeta_miniMax(self, nodo, profundidade, alpha, beta, maximizandoJogador):
        melhorValor = None

        if nodo._isNodoFolha or profundidade == 0:
            nodo._heuristica = self._heuristc.computarHeuristicaTabuleiro(nodo, self.gerarIndicesPossiveisDeJogadaOtimiz(nodo._board))
            return nodo._heuristica, nodo

        elif maximizandoJogador:
            melhorValor = alpha
            for indice in self.gerarIndicesPossiveisDeJogadaOtimiz(nodo._board):
                nodoFilho = self.criarNodoFilho(nodo._board, indice, Peca.COMPUTADOR, profundidade - 1)
                valorFilho, nodoRetornado = self.alphabeta_miniMax(nodoFilho, profundidade - 1, melhorValor, beta, False)
                # aqui ele tá retornando só o valor, não o objeto
                melhorValor = max(melhorValor, valorFilho)
                if beta <= melhorValor:
                    break

        else:
            melhorValor = beta
            for indice in self.gerarIndicesPossiveisDeJogadaOtimiz(nodo._board):
                nodoFilho = self.criarNodoFilho(nodo._board, indice, Peca.JOGADOR, profundidade - 1)
                valorFilho, nodoRetornado = self.alphabeta_miniMax(nodoFilho, profundidade - 1, alpha, melhorValor, True)
                # aqui ele tá retornando só o valor, não o objeto
                melhorValor = min(melhorValor, valorFilho)
                if melhorValor <= alpha:
                    break

        return melhorValor, nodoRetornado

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

    def criarNodoFilho(self, board, indice, pecaJogada, profundidade):
        linha, coluna = Utils.parserJogada(str(indice))
        index = int(str(linha) + str(coluna))

        tabuleiro = copy.deepcopy(board)
        tabuleiro[linha][coluna] = pecaJogada

        isNodoFolha = self.analisaAdjacenciasPecaJogada(tabuleiro, linha, coluna, pecaJogada)
        return Nodo(index, tabuleiro, pecaJogada, None, profundidade, isNodoFolha)

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
            if indLinha - 1 < 0 or indColuna + 1 > 6:
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
            if indLinha - 1 < 0 or indColuna - 1 < 0:
                return False

        return sequencia == 4
