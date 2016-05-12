# coding: utf-8


class Utils(object):

    @staticmethod
    def printEstadoTabuleiro(tab):
        tabsFormat = '\t \t \t \t \t \t \t \t \t  '

        for i in xrange(len(tab)):
            print tabsFormat, '---------------------------------------------------------'
            print tabsFormat, '|', tab[i][0], '|', tab[i][1], '|', tab[i][2], '|', tab[i][3], '|', tab[i][4], '|', tab[i][5], '|', tab[i][6], '|'
        print tabsFormat, '---------------------------------------------------------'

    @staticmethod
    # ToDo
    def descobrePosicoesDisponiveisTabuleiro(tab):
        posicoesDisponiveis = [51, 52, 53, 54, 55, 56]
        return posicoesDisponiveis
