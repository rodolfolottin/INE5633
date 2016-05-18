# coding: utf-8
class Heuristica(object):

    def __init__(self):
        pass

    def retornaToposTabuleiro(self, lista):
        topos = []

        for num in lista:
            numStr = str(num)
            if max(5, int(numStr[0]) + 1) == 5:
                linha, coluna = int(numStr[0]) + 1, int(numStr[1])
                topos.append((linha, coluna))

        return topos

    def analisaColunaPecaTopo(self, tabuleiro, peca):
        linha = peca[0]
        coluna = peca[1]
        listaSequencias = []
        sequencia = 1

        for indiceLinha in xrange(linha + 1, 6, 1):
            if tabuleiro[indiceLinha - 1][coluna] == tabuleiro[indiceLinha][coluna]:
                sequencia += 1
                if sequencia == 4 or max(5, indiceLinha + 1) == 6:
                    # identificador do jogador
                    listaSequencias.append(tabuleiro[indiceLinha - 1][coluna])
                    listaSequencias.append(sequencia)
                    break
            else:
                if sequencia > 1:
                    listaSequencias.append(tabuleiro[indiceLinha - 1][coluna])
                    listaSequencias.append(sequencia)
                else:
                    sequencia = 0
                break

        return listaSequencias
