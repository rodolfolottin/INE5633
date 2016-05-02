# coding: utf-8
from Utils import Utils
import argparse
from random import randint


class Ligue4(object):

    _pecaVazia = '     '

    def __init__(self, modo, nomeJogador):
        self._tabuleiro = [[self._pecaVazia for x in xrange(6)] for y in xrange(7)]
        self._posicoesDisponiveis = Utils.descobrePosicoesDisponiveisTabuleiro(self._tabuleiro)
        self._jogador = nomeJogador

        if randint(0, 2) == 0:
            self._jogadorDaVez = 'Computador'
        else:
            self._jogadorDaVez = self._jogador

        if modo == 'dificil':
            self._profundidade = 6
        elif modo == 'normal':
            self._profundidade = 4
        else:
            self._profundidade = 2

    def _atualizaJogada(self):
        if self._jogadorDaVez == 'Computador':
            self._jogadorDaVez = self._jogador
        else:
            self._jogadorDaVez = 'Computador'
        self._posicoesDisponiveis = Utils.descobrePosicoesDisponiveisTabuleiro(self._tabuleiro)

    def run(self):
        print '\t \t \t \t \t \t \t ##############################################################'
        self._posicoesDisponiveis = Utils.descobrePosicoesDisponiveisTabuleiro(self._tabuleiro)

        while True:
            print 'Jogador da vez:', self._jogadorDaVez
            if self._jogadorDaVez == self._jogador:
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
                # call algoritmo Minimax, imprimir tabuleiro antes ou depois da jogada?
                Utils.printEstadoTabuleiro(self._tabuleiro)
                # Acabou jogada, passa vez
                self._atualizaJogada()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emula o jogo Ligue4 (Jogador vs Computador). Foi utilizado o algoritmo Minimax com poda alfa e beta para implementação das jogadas do computador.')
    parser.add_argument('-modo', type=str, choices=list(('facil', 'normal', 'dificil')), help="Um modo de jogo entre: facil, normal e dificil.")
    parser.add_argument('-nome', type=str, help="Seu nome.")

    args = parser.parse_args()
    Ligue4(args.modo, args.nome).run()
