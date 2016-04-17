#coding: utf-8

class Utils(object):

    @staticmethod
    def exibirRelatorio(nodoAnalisado):

        while nodoAnalisado != None:
            Utils.exibirEstadoDoNodo(nodoAnalisado)
            nodoAnalisado = nodoAnalisado.nodoPai

    @staticmethod
    def exibirEstadoDoNodo(nodoAnalisado):
        j = 1

        tabuleiro = nodoAnalisado.estadoTabuleiro
        profundidade = nodoAnalisado.profundidade
        heuristicaTotal = nodoAnalisado.heuristicaCaminho()

        for i in (1, 2, 3):
            print('- - - - - - - - - -')
            print('|  ' + str(tabuleiro['a' + str(i) + str(j)]) + '  |  ' + str(tabuleiro['a' + str(i) + str(j + 1)]) + '  |  ' + str(tabuleiro['a' + str(i) + str(j + 2)]) + '  |')
        print('- - - - - - - - - -')
        print('Profundidade: ' + str(profundidade))
        print('Heurística Total: ' + str(heuristicaTotal))
