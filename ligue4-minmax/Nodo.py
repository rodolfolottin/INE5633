# coding: utf-8


class Nodo(object):

    """docstring for Nodo"""
    def __init__(self, repre, index):
        self._repre = repre
        self._index = index

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  'Índice de substituição:', self._index)
