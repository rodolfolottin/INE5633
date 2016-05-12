# coding: utf-8


class Nodo(object):

    def __init__(self, index, heuristica, utilidade):
        self._index = index
        self._heuristica = heuristica
        self._utilidade = utilidade
        self._isNodoFolha = False

    def __repr__(self):
        return '{}: {} {} {} {} {} {}'.format(self.__class__.__name__,
                                              'Índice de substituição:', self._index,
                                              'Heurística:', self._heuristica,
                                              'Utilidade:', self._utilidade,
                                              'isNodoFolha:', self._isNodoFolha)
