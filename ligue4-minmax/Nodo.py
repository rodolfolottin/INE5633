# coding: utf-8


class Nodo(object):

    def __init__(self, index, board, peca, heuristica, profundidade, isNodoFolha):
        self._index = index
        self._board = board
        self._peca = peca
        self._heuristica = heuristica
        self._profundidade = profundidade
        self._isNodoFolha = isNodoFolha

    def __repr__(self):
        return '{}: {} {} {} {} {} {} {} {}'.format(self.__class__.__name__,
                                                    'Índice de substituição:', self._index,
                                                    'Board:', self._board,
                                                    'Peca:', self._peca,
                                                    'Heurística:', self._heuristica,
                                                    'Profundidade', self._profundidade,
                                                    'isNodoFolha:', self._isNodoFolha)
