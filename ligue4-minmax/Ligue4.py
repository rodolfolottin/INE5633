# coding: utf-8
from Utils import Utils
from Peca import Peca
from Nodo import Nodo
from Minimax import Minimax
from random import randint
import argparse
import os


class Ligue4(object):

    def __init__(self, nomeJogador, modo):
        self._tabuleiro = []
        for i in range(6):
            self._tabuleiro.append([])
            for j in range(7):
                self._tabuleiro[i].append(Peca.VAZIA)
        self._jogador = nomeJogador
        self._posicoesDisponiveis = []
        self._lenTab = len(self._tabuleiro)
        self._minMax = Minimax(self._tabuleiro, self._lenTab)
        self._profundidade = self.setaDificuldadeJogo(modo)
        self._vitoria = False

        if randint(0, 1) == 0:
            self._jogadorDaVez = 'IA'
        else:
            self._jogadorDaVez = self._jogador

        os.system(['clear', 'cls'][os.name == 'nt'])
        print("Bem-vindo ao jogo {}! Seu objetivo é formar 4 em linha, coluna ou diagonal antes da IA. ".format(self.__class__.__name__))

    def setaDificuldadeJogo(self, modo):
        if modo.lower() == 'facil':
            return 3
        elif modo.lower() == 'dificil':
            return 5
        else:
            return 4

    def _alteraJogadorDaVez(self):
        if self._jogadorDaVez == 'IA':
            self._jogadorDaVez = self._jogador
        else:
            self._jogadorDaVez = 'IA'

        self._posicoesDisponiveis = self._minMax.gerarIndicesPossiveisDeJogada(self._tabuleiro)

    def atualizaEstadoTabuleiro(self, posicaoJogada, pecaJogador):
        linha, coluna = Utils.parserJogada(posicaoJogada)
        self._tabuleiro[linha][coluna] = pecaJogador
        self._vitoria = self._minMax.analisaAdjacenciasPecaJogada(self._tabuleiro, linha, coluna, pecaJogador)
        self._alteraJogadorDaVez()
        Utils.printEstadoTabuleiro(self._tabuleiro)

    def run(self):
        print '\t \t \t \t \t \t \t \t \t ##############################################################'
        self._posicoesDisponiveis = self._minMax.gerarIndicesPossiveisDeJogada(self._tabuleiro)

        # primeira impressão
        if self._jogadorDaVez == self._jogador:
            Utils.printEstadoTabuleiro(self._tabuleiro)

        while True and not self._vitoria:
            print 'Jogador da vez:', self._jogadorDaVez
            if self._jogadorDaVez == self._jogador:
                input_msg = 'Em que posicao você deseja jogar? ' + str(self._posicoesDisponiveis) + '\n'

                try:
                    jogada = int(raw_input(input_msg))
                    if jogada not in self._posicoesDisponiveis:
                        print 'A posição fornecida não é uma das posições disponíveis'
                        continue
                except ValueError:
                    print 'A posição fornecida não é um número'
                    jogada = None
                    continue

                self.atualizaEstadoTabuleiro(str(jogada), Peca.JOGADOR)

            else:
                # tabuleiro = [[y for y in x] for x in self._tabuleiro]
                # nodo = Nodo(None, tabuleiro, None, None, 1, False)
                # jogada, nodo = self._minMax.alphabeta_miniMax(nodo, 1, -999999999, 999999999, True)
                # print jogada, nodo._board

                # test purposes
                jogada = self._posicoesDisponiveis[randint(0, len(self._posicoesDisponiveis) - 1)]
                self.atualizaEstadoTabuleiro(str(jogada), Peca.COMPUTADOR)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emula o jogo Ligue4 (Jogador vs IA). Foi utilizado o algoritmo Minimax com poda alfa e beta para implementação das jogadas da IA.')
    parser.add_argument('nome', type=str, help="Nome do jogador que disputará contra a IA.")
    parser.add_argument('-modo', type=str, choices=list(('facil', 'normal', 'dificil')), help="Um modo de dificuldade do jogo.")

    args = parser.parse_args()

    Ligue4(args.nome, args.modo).run()
