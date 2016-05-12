# coding: utf-8
from Peca import Peca


class Utils(object):

    @staticmethod
    def printEstadoTabuleiro(tab):
        tabsFormat = '\t \t \t \t \t \t \t \t \t  '

        for i in xrange(len(tab)):
            print tabsFormat, '---------------------------------------------------------'
            print tabsFormat, '|', Peca.toString(tab[i][0]), '|', Peca.toString(tab[i][1]), '|', Peca.toString(tab[i][2]), '|', Peca.toString(tab[i][3]), '|', Peca.toString(tab[i][4]), '|', Peca.toString(tab[i][5]), '|', Peca.toString(tab[i][6]), '|'
        print tabsFormat, '---------------------------------------------------------'
