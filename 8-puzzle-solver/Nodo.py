#coding: utf-8

class Nodo(object):

    def __init__(self, estadoTabuleiro, pesoHeuristica, profundidade, nodoPai):
        self.estadoTabuleiro = estadoTabuleiro
        self.pesoHeuristica = pesoHeuristica
        self.profundidade = profundidade
        self.nodoPai = nodoPai

    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                  'Estado Tabuleiro: ' + str(self.estadoTabuleiro),
                                  'pesoHeuristica: ' + str(self.pesoHeuristica),
                                  'Profundidade: ' + str(self.profundidade),
                                  'Nodo pai: ' + str(self.nodoPai))
    def heuristicaCaminho(self):
      return self.pesoHeuristica + self.profundidade