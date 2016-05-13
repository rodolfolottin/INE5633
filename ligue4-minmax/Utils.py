# coding: utf-8
from Peca import Peca


class Utils(object):

    @staticmethod
    def printEstadoTabuleiro(tab):
        tabsFormat = '\t \t \t \t \t \t \t \t \t  '

        for i in xrange(len(tab)):
            print tabsFormat, '---------------------------------------------------------'
            print tabsFormat, '|', Peca.toStr(tab[i][0]), '|', Peca.toStr(tab[i][1]), '|', Peca.toStr(tab[i][2]), '|', Peca.toStr(tab[i][3]), '|', Peca.toStr(tab[i][4]), '|', Peca.toStr(tab[i][5]), '|', Peca.toStr(tab[i][6]), '|'
        print tabsFormat, '---------------------------------------------------------'
