# coding: utf-8


class Utils(object):

    @staticmethod
    def printEstadoTabuleiro(tab):
        tabsFormat = '\t \t \t \t \t \t \t \t'

        for i in xrange(len(tab)):
            print tabsFormat, '-------------------------------------------'
            print tabsFormat, '|', tab[i][0], '|', tab[i][1], '|', tab[i][2], '|', tab[i][3], '|', tab[i][4], '|', tab[i][5], '|'
        print tabsFormat, '-------------------------------------------'
