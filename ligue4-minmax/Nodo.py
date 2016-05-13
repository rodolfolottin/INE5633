# coding: utf-8


class Nodo(object):

    def __init__(self, index, board, heuristica, utilidade, isNodoFolha):
        self._index = index
        self._board = board
        self._heuristica = heuristica
        self._utilidade = utilidade
        self._isNodoFolha = isNodoFolha

    def __repr__(self):
        return '{}: {} {} {} {} {} {}'.format(self.__class__.__name__,
                                              'Índice de substituição:', self._index,
                                              'Heurística:', self._heuristica,
                                              'Utilidade:', self._utilidade,
                                              'isNodoFolha:', self._isNodoFolha)
