# debugging purposes
from Utils import Utils
from Peca import Peca

class Minimax(object):

    def __init__(self, tab):
        self._tab = tab

    def alphabeta_miniMax(self, nodo, profundidade, alpha, beta, maximizandoJogador):
        melhorValor = None

        if nodo._isNodoFolha or profundidade == 0:
            # computar heuristica e utilidade
            melhorValor = nodo

        elif maximizandoJogador:
            melhorValor = alpha
            for indices in self.gerarIndicesPossiveisDeJogada(self._tab):
                valorFilho = self.alphabeta_miniMax(filho, profundidade - 1, melhorValor, beta, False)
                melhorValor = max(melhorValor, valorFilho)
                if beta <= melhorValor:
                    break

        else:
            melhorValor = beta
            for indices in self.gerarIndicesPossiveisDeJogada(self._tab):
                valorFilho = self.alphabeta_miniMax(filho, profundidade - 1, alpha, melhorValor, True)
                melhorValor = min(melhorValor, valorFilho)
                if melhorValor <= alpha:
                    break

        return melhorValor

    def gerarIndicesPossiveisDeJogada(self, tab):
        indicesPossiveis = []
        colunasIrrelv = []

        for linha in xrange(len(tab) - 1, - 1, - 1):
            for coluna in xrange(len(tab[linha]) - 1, - 1, - 1):
            	if coluna not in colunasIrrelv:
                    if tab[linha][coluna] == Peca.VAZIA:
						colunasIrrelv.append(coluna)
						indicesPossiveis.append(int(str(linha) + str(coluna)))

        return indicesPossiveis
