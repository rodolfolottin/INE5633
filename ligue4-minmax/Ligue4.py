# coding: utf-8
import argparse


class Ligue4(object):

    def __init__(self, modo):
        self._modo = modo
        self._tabuleiro = [[None for x in xrange(6)] for y in xrange(7)]
        self._profundidade = self._profundidadeModo(modo)
        self._jogadorDaVez

    def _profundidadeModo(self, dificuldade):
        if dificuldade == 'dificil':
            self._profundidade = 6
        elif dificuldade == 'normal':
            self._profundidade = 4
        else:
            self._profundidade = 2

    def run(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emula o jogo Ligue4 (Jogador vs Computador). Foi utilizado o algoritmo Minimax com poda alfa e beta para implementação das jogadas do computador.')
    parser.add_argument('-m', type=str, help="Um modo de jogo entre: fácil, normal e difícil")

    args = parser.parse_args()
    Ligue4(args.m).run()
