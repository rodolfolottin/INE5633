class Peca(object):

    VAZIA = 0
    JOGADOR = 1
    COMPUTADOR = 2

    @staticmethod
    def toString(i):
        if i == 0:
            return '     '
        elif i == 1:
            return u"\033[1;31;48m  \u25CF  \033[0m"
        else:
            return u"\033[1;34;48m  \u25CF  \033[0m"
