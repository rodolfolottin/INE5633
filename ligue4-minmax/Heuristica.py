# coding: utf-8
from Peca import Peca


class Heuristica(object):

    def __init__(self):
        pass

    def retornaToposTabuleiro(self, lista):
        topos = []

        for num in lista:
            numStr = str(num)
            if max(5, int(numStr[0]) + 1) == 5:
                topos.append(int(str(int(numStr[0]) + 1) + numStr[1]))

        return topos
















