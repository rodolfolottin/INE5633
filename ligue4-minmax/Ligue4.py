# coding: utf-8
import argparse
from random import randint


class Ligue4(object):

    def __init__(self, modo):
        self._modo = modo
        self._tabuleiro = [[None for x in xrange(6)] for y in xrange(7)]
        self._profundidade = self._profundidadeModo(modo)
        self._posicoesDisponiveis = None
        self._jogadorDaVez = 'Jogador'

        if randint(0, 1) == 0:
            self._jogadorDaVez = 'Computador'

    def _profundidadeModo(self, dificuldade):
        if dificuldade == 'dificil':
            self._profundidade = 6
        elif dificuldade == 'normal':
            self._profundidade = 4
        else:
            self._profundidade = 2

    # ToDo implementar função
    # def _descobrePosicoesDisponiveisTabuleiro(self):
    #     for linha in self._tabuleiro:
    #         print linha

    def _atualizaJogada(self):
        self._descobrePosicoesDisponiveisTabuleiro()
        # se jogadorDaVez for Computador, passa a ser Player, se não passa a ser Computador
        if self._jogadorDaVez == 'Computador':
            self._jogadorDaVez = 'Jogador'
        else:
            self._jogadorDaVez = 'Computador'

    def run(self):
        self._descobrePosicoesDisponiveisTabuleiro()

        while True:
            if self._jogadorDaVez == 'Jogador':
                input_msg = 'Em que posicao você deseja jogar? ' + str(self._posicoesDisponiveis)

                try:
                    jogada = int(raw_input(input_msg))
                    if jogada not in self._posicoesDisponiveis:
                        print 'A posição fornecida não é uma das posições disponíveis'
                except ValueError:
                    print 'A posição fornecida não é um número fornecido não é um número'
                    jogada = None
                    continue
                # Acabou jogada, passa vez
                self._atualizaJogada()
            else:
                'Print Rodolfo'
                # Acabou jogada, passa vez
                self._atualizaJogada()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emula o jogo Ligue4 (Jogador vs Computador). Foi utilizado o algoritmo Minimax com poda alfa e beta para implementação das jogadas do computador.')
    parser.add_argument('-m', type=str, help="Um modo de jogo entre: fácil, normal e difícil")

    args = parser.parse_args()
    Ligue4(args.m).run()
