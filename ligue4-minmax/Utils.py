# coding: utf-8
from Peca import Peca


class Utils(object):

    @staticmethod
    def printEstadoTabuleiro(tab):
        tabsFormat = '\t \t \t \t \t \t \t \t \t  '
        tabsFormatRow = '\t \t \t \t \t \t \t \t \t '

        print tabsFormat, '    0       1       2       3       4       5       6'
        for i in xrange(len(tab)):
            print tabsFormat, '---------------------------------------------------------'
            print tabsFormatRow + str(i), '|', Peca.toStr(tab[i][0]), '|', Peca.toStr(tab[i][1]), '|', Peca.toStr(tab[i][2]), '|', Peca.toStr(tab[i][3]), '|', Peca.toStr(tab[i][4]), '|', Peca.toStr(tab[i][5]), '|', Peca.toStr(tab[i][6]), '|'
        print tabsFormat, '---------------------------------------------------------'

    @staticmethod
    def parserJogada(indiceJogada):
        if len(indiceJogada) == 2:
            linha = int(indiceJogada[0])
            coluna = int(indiceJogada[1])
        else:
            # problema com 01, 02, 03...
            linha = int(0)
            coluna = int(indiceJogada)
        return linha, coluna
