class Peca(object):

    VAZIA = 0
    JOGADOR = 1
    COMPUTADOR = 2

    @staticmethod
    def toString(i):
        if i == 0:
            return '     '
        elif i == 1:
            return '  X  '
        else:
            return '  O  '
