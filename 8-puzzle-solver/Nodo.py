#coding: utf-8

class Nodo(object):

    def __init__(self, estadoTabuleiro):
        self.estadoTabuleiro = estadoTabuleiro
        self.pesoHeuristica = 0
        self.profundidade = 0
        self.nodoPai = None

    def __str__(self):
        return ""