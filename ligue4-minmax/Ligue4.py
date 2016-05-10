# coding: utf-8
from Utils import Utils
from Peca import Peca
from Minimax import Minimax
from random import randint
import argparse
import os


class Ligue4(object):

    def __init__(self, nomeJogador):
        self._tabuleiro = []
        for i in range(7):
            self._tabuleiro.append([])
            for j in range(7):
                self._tabuleiro[i].append(Peca.VAZIA)
        self._jogador = nomeJogador
        self._posicoesDisponiveis = []
        self._minMax = Minimax(5)

        if randint(0, 2) == 0:
            self._jogadorDaVez = 'Computador'
        else:
            self._jogadorDaVez = self._jogador

        os.system(['clear', 'cls'][os.name == 'nt'])
        print("Bem-vindo ao jogo {}! Seu objetivo é formar 4 em linha, coluna ou diagonal antes da IA. ".format(self.__class__.__name__))

    def _alteraJogadorDaVez(self):
        if self._jogadorDaVez == 'Computador':
            self._jogadorDaVez = self._jogador
        else:
            self._jogadorDaVez = 'Computador'
        self._posicoesDisponiveis = Utils.descobrePosicoesDisponiveisTabuleiro(self._tabuleiro)

    def colocaPecaNaPosicao(self, posicaoJogada, pecaJogador):
        linha = int(posicaoJogada[0])
        coluna = int(posicaoJogada[1])
        self._tabuleiro[linha][coluna] = pecaJogador

        self._alteraJogadorDaVez()

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
                    print 'A posição fornecida não é um número'
                    jogada = None
                    continue

                self.colocaPecaNaPosicao(str(jogada), Peca.JOGADOR)
            else:
                # call algoritmo Minimax, imprimir tabuleiro antes ou depois da
                # jogada?
                Utils.printEstadoTabuleiro(self._tabuleiro)

                # test
                self.colocaPecaNaPosicao(str(00), Peca.COMPUTADOR)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emula o jogo Ligue4 (Jogador vs Computador). Foi utilizado o algoritmo Minimax com poda alfa e beta para implementação das jogadas do computador.')
    parser.add_argument('nome', type=str, help="Nome do jogador que disputará contra a IA.")
    # parser.add_argument('-modo', type=str, choices=list(('facil', 'normal', 'dificil')), help="Um modo de dificuldade do jogo.")

    args = parser.parse_args()

    # Ligue4(args.modo, args.nome).run()
    Ligue4(args.nome).run()
