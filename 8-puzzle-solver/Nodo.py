#coding: utf-8

class Nodo(object):

    def __init__(self, estadoTabuleiro):
        self.estadoTabuleiro = estadoTabuleiro
        self.pesoHeuristica = 0
        self.profundidade = 0
        self.nodoPai = None

    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                  self.estadoTabuleiro,
                                  self.pesoHeuristica,
                                  self.profundidade,
                                  self.nodoPai)

    # Docstrings: Função utilizada para imprimir um espaço de estado do quebra cabeça de 8 peças
    def exibirEstadoDoNodo(self):
        j = 1

        tabuleiro = self.estadoTabuleiro

        for i in (1, 2, 3):
            print('- - - - - - - - - -')
            print('|  ' + str(tabuleiro['a' + str(i) + str(j)]) + '  |  ' + str(tabuleiro['a' + str(i) + str(j + 1)]) + '  |  ' + str(tabuleiro['a' + str(i) + str(j + 2)]) + '  |')
        print('- - - - - - - - - -')