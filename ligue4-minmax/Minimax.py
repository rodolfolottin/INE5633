from Utils import Utils
from Peca import Peca


class Minimax(object):

    def __init__(self):
        pass

    def alphabeta_miniMax(self, nodo, profundidade, alpha, beta, maximizandoJogador):
        melhorValor = None

        if nodo._isNodoFolha or profundidade == 0:
            # computar heuristica e utilidade
            melhorValor = nodo

        elif maximizandoJogador:
            melhorValor = alpha

            # gerar filhos aqui
            for filho in nodo._filhos:
                valorFilho = self.alphabeta_miniMax(filho, profundidade - 1, melhorValor, beta, False)
                melhorValor = max(melhorValor, valorFilho)
                if beta <= melhorValor:
                    break

        else:
            melhorValor = beta

            # gerar filhos aqui
            for filho in nodo._filhos:
                valorFilho = self.alphabeta_miniMax(filho, profundidade - 1, alpha, melhorValor, True)
                melhorValor = min(melhorValor, valorFilho)
                if melhorValor <= alpha:
                    break

        return melhorValor

    def gerarIndicesPossiveisDeJogada(self, tab):

        # test purposes
        tab[5][0] = Peca.JOGADOR
        tab[4][0] = Peca.COMPUTADOR
        tab[3][0] = Peca.COMPUTADOR

        for linha in xrange(len(tab) - 1, - 1, - 1):
            for coluna in xrange(len(tab[linha]) - 1, - 1, - 1):
                if tab[linha][coluna] != Peca.VAZIA:
                    print linha, coluna

        Utils.printEstadoTabuleiro(tab)
