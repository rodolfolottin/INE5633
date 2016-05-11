class Minimax(object):

    def __init__(self, profundidade):
        self.profundidade = profundidade

    def alphabeta_miniMax(self, nodo, profundidade, alpha, beta, maximizandoJogador):
        melhorValor = None

        if nodo._isNodoFolha:
            melhorValor = nodo

        elif maximizandoJogador:
            melhorValor = alpha

            for filho in nodo._filhos:
                valorFilho = self.alphabeta_miniMax(filho, profundidade - 1, melhorValor, beta, False)
                melhorValor = max(melhorValor, valorFilho)
                if beta <= melhorValor:
                    break

        else:
            melhorValor = beta

            for filho in nodo._filhos:
                valorFilho = self.alphabeta_miniMax(filho, profundidade - 1, alpha, melhorValor, True)
                melhorValor = min(melhorValor, valorFilho)
                if melhorValor <= alpha:
                    break

        return melhorValor
