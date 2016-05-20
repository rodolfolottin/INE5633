# coding: utf-8
from Peca import Peca
from Nodo import Nodo

class Heuristica(object):

    def __init__(self):
        pass

    def retornaToposTabuleiro(self, lista):
        topos = []

        for num in lista:
            numStr = str(num)
            if max(5, int(numStr[0]) + 1) == 5:
                if len(numStr) < 2:
                    # problema com 00
                    numStr += str(0)
                linha, coluna = int(numStr[0]) + 1, int(numStr[1])
                topos.append((linha, coluna))

        return topos

    def computarHeuristicaTabuleiro(self, nodo, possiveisMovimentos):
        pecasAnalisaveis = self.retornaToposTabuleiro(possiveisMovimentos)
        pontuacao = 0

        if nodo._isNodoFolha:
            if nodo._peca == Peca.COMPUTADOR:
                pontuacao = 10 ** 4 - nodo._profundidade * 25
            elif nodo._peca == Peca.JOGADOR:
                pontuacao = -10 ** 4 - nodo._profundidade * 25
        else:
            for peca in pecasAnalisaveis:
                pontComp, pontJog = self.calcularHeuristicas(nodo._board, peca)
                pontuacao += pontComp
                pontuacao -= pontJog

        return pontuacao - nodo._profundidade * 25

    def calcularHeuristicas(self, tabuleiro, peca):
        listaSequencias = self.retornaSequencias(tabuleiro, peca)
        pontComp = 0
        pontJog = 0

        for sequencias in listaSequencias:
            for sequencia in sequencias:
                if sequencia:
                    # pontuação computador
                    if sequencia[0] == Peca.COMPUTADOR:
                        if sequencia[1] == 4:
                            pontComp += 10 ** 4
                        elif sequencia[1] == 3:
                            pontComp += 10 ** 3
                        elif sequencia[1] == 2:
                            pontComp += 10 ** 2
                    # pontuação jogador
                    elif sequencia[0] == Peca.JOGADOR:
                        if sequencia[1] == 4:
                            pontJog += 10 ** 4
                        elif sequencia[1] == 3:
                            pontJog += 10 ** 3
                        elif sequencia[1] == 2:
                            pontJog += 10 ** 2

        return pontComp, pontJog

    def retornaSequencias(self, tabuleiro, peca):
        listaSequencias = []
        listaSequencias.append(self.analisaColunaPecaTopo(tabuleiro, peca))
        listaSequencias.append(self.analisaLinhaPecaTopo(tabuleiro, peca))
        listaSequencias.append(self.analisaDiagDirPecaTopo(tabuleiro, peca))
        listaSequencias.append(self.analisaDiagEsqPecaTopo(tabuleiro, peca))

        return listaSequencias

    def analisaColunaPecaTopo(self, tabuleiro, peca):
        linha = peca[0]
        coluna = peca[1]
        listaSequencias = []
        sequencia = 1
        listaSeq = []

        for indiceLinha in xrange(linha + 1, 6, 1):
            if tabuleiro[indiceLinha - 1][coluna] == tabuleiro[indiceLinha][coluna]:
                sequencia += 1
                if sequencia == 4 or max(5, indiceLinha + 1) == 6:
                    # identificador do jogador
                    listaSeq.append(tabuleiro[indiceLinha - 1][coluna])
                    listaSeq.append(sequencia)
                    break
            else:
                if sequencia > 1:
                    listaSeq.append(tabuleiro[indiceLinha - 1][coluna])
                    listaSeq.append(sequencia)
                else:
                    sequencia = 0
                break

        listaSequencias.append(listaSeq)

        return listaSequencias

    def analisaLinhaPecaTopo(self, tabuleiro, peca):
        lista = []
        linha = peca[0]
        coluna = peca[1]

        for indiceColuna in xrange(7):
            lista.append(tabuleiro[linha][indiceColuna])

        return self._analiseGenericaLista(lista)

    def analisaDiagDirPecaTopo(self, tabuleiro, peca):
        lista = []
        limiteBoard = False
        indLinha = peca[0]
        indColuna = peca[1]

        while not limiteBoard:
            if max(5, indLinha + 1) == 5 and max(6, indColuna + 1) == 6:
                indLinha += 1
                indColuna += 1
            else:
                break

        for x in range(0, 6):
            lista.append(tabuleiro[indLinha][indColuna])
            indLinha -= 1
            indColuna -= 1
            if indLinha < 0 or indColuna < 0: break

        return self._analiseGenericaLista(lista)

    def analisaDiagEsqPecaTopo(self, tabuleiro, peca):
        lista = []
        limiteBoard = False
        indLinha = peca[0]
        indColuna = peca[1]

        while not limiteBoard:
            if max(5, indLinha + 1) == 5 and min(0, indColuna - 1) == 0:
                indLinha += 1
                indColuna -= 1
            else:
                break

        for x in range(0, 6):
            lista.append(tabuleiro[indLinha][indColuna])
            indLinha -= 1
            indColuna += 1

            if indLinha < 0 or indColuna > 6: break

        return self._analiseGenericaLista(lista)

    def _analiseGenericaLista(self, lista):
        listasSequencias = []
        # 7 -> 4 | 6 -> 3 | 5 -> 2 | 4 -> 1
        for quantidadeQuadruplas in xrange(len(lista) - 3):
            listaSeq = []
            sequencia = 1
            pecaSeq = None
            primeira = True
            for indiceColuna in xrange(0, 4):
                if lista[indiceColuna] != Peca.VAZIA:
                    if primeira:
                        primeira = False
                        pecaSeq = lista[indiceColuna]
                        continue
                    if pecaSeq == lista[indiceColuna]:
                        sequencia += 1
                    else: break
                if indiceColuna == 3 and sequencia > 1:
                    # identifica jogador
                    listaSeq.append(pecaSeq)
                    listaSeq.append(sequencia)

            if listaSeq:
                listasSequencias.append(listaSeq)
            lista.pop(0)

        return listasSequencias
