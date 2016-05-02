# coding: utf-8
from Utils import Utils
import argparse
from random import randint


class Ligue4(object):

    _VAZIO = '    '

    def __init__(self, modo):
        self._modo = modo
        self._tabuleiro = [[self._VAZIO for x in xrange(6)] for y in xrange(7)]
        self._profundidade = self._profundidadeModo(modo)
        self._posicoesDisponiveis = list()
        self._jogadorDaVez = 'Jogador'

        if randint(0, 2) == 0:
            self._jogadorDaVez = 'Computador'

    def _profundidadeModo(self, dificuldade):
        if dificuldade == 'dificil':
            self._profundidade = 6
        elif dificuldade == 'normal':
            self._profundidade = 4
        else:
            self._profundidade = 2

    # ToDo
    def _descobrePosicoesDisponiveisTabuleiro(self):
        print 'self._jogadorDaVez', self._jogadorDaVez
        self._posicoesDisponiveis = list()
        for linha in self._tabuleiro:
            print linha

    def _atualizaJogada(self):
        if self._jogadorDaVez == 'Computador':
            self._jogadorDaVez = 'Jogador'
        else:
            self._jogadorDaVez = 'Computador'
        self._descobrePosicoesDisponiveisTabuleiro()

    def run(self):
        self._descobrePosicoesDisponiveisTabuleiro()

        while True:
            print '\t \t \t \t \t \t \t #########################################################'
            if self._jogadorDaVez == 'Jogador':
                input_msg = 'Em que posicao você deseja jogar? ' + str(self._posicoesDisponiveis) + '\n'

                Utils.printEstadoTabuleiro(self._tabuleiro)

                try:
                    jogada = int(raw_input(input_msg))
                    if jogada not in self._posicoesDisponiveis:
                        print 'A posição fornecida não é uma das posições disponíveis'
                        continue
                except ValueError:
                    print 'A posição fornecida não é um número fornecido não é um número'
                    jogada = None
                    continue
                # Acabou jogada, passa vez
                self._atualizaJogada()
            else:
                Utils.printEstadoTabuleiro(self._tabuleiro)
                # Acabou jogada, passa vez
                self._atualizaJogada()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emula o jogo Ligue4 (Jogador vs Computador). Foi utilizado o algoritmo Minimax com poda alfa e beta para implementação das jogadas do computador.')
    parser.add_argument('-m', type=str, help="Um modo de jogo entre: fácil, normal e difícil")

    args = parser.parse_args()
    Ligue4(args.m).run()
