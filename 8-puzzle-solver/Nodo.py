#coding: utf-8

class Nodo(object):

    heuristicaCaminho = self.pesoHeuristica + self.profundidade

    def __init__(self, estadoTabuleiro, pesoHeuristica, profundidade, nodoPai):
        self.estadoTabuleiro = estadoTabuleiro
        self.pesoHeuristica = pesoHeuristica
        self.profundidade = profundidade
        self.nodoPai = nodoPai

    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                  self.estadoTabuleiro,
                                  self.pesoHeuristica,
                                  self.profundidade,
                                  self.nodoPai)