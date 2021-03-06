# coding: utf-8
from Utils import Utils
from Peca import Peca
from Nodo import Nodo
from Minimax import Minimax
from random import randint
import argparse
import os
import copy


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
        self._modo = modo
        self._profundidade = self.setaDificuldadeJogo(modo)
        self._minMax = Minimax(self._tabuleiro, self._lenTab, self._profundidade)
        self._vitoria = False
        self._jogadorVencedor = None
        self._count = 0

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
            return 6
        else:
            return 4

    def _alteraJogadorDaVez(self):
        if self._jogadorDaVez == 'IA':
            self._jogadorDaVez = self._jogador
        else:
            self._jogadorDaVez = 'IA'
        self._count += 1
        self._posicoesDisponiveis = self._minMax.gerarIndicesPossiveisDeJogada(self._tabuleiro)

    def _analisaProfundidadeDinamica(self):
        if self._count > 15 and self._profundidade > 4 and self._profundidade < 9:
            self._profundidade = 9

    def atualizaEstadoTabuleiro(self, posicaoJogada, pecaJogador):
        linha, coluna = Utils.parserJogada(posicaoJogada)
        self._tabuleiro[linha][coluna] = pecaJogador
        Utils.printEstadoTabuleiro(self._tabuleiro)
        self._vitoria = self._minMax.verificaVitoriaPecaJogada(self._tabuleiro, linha, coluna, pecaJogador)
        self._analisaProfundidadeDinamica()
        if self._vitoria:
            if pecaJogador == 1:
                self._jogadorVencedor = self._jogador
            else:
                self._jogadorVencedor = 'IA'
        self._alteraJogadorDaVez()

    def criaNodoAtual(self):
        return Nodo(None, copy.deepcopy(self._tabuleiro), None, None, 0, False, -9999999999, 9999999999)

    def run(self):
        print '\t \t \t \t \t \t \t \t \t ##############################################################'
        self._posicoesDisponiveis = self._minMax.gerarIndicesPossiveisDeJogada(self._tabuleiro)

        # primeira impressão
        if self._jogadorDaVez == self._jogador:
            Utils.printEstadoTabuleiro(self._tabuleiro)

        while True:
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
                nodo, iteracoes = self._minMax.callMinimax(self.criaNodoAtual(), 0)
                jogada = nodo._index

                print 'Quantidade iterações até jogada:', iteracoes

                self.atualizaEstadoTabuleiro(str(jogada), Peca.COMPUTADOR)

            if self._vitoria:
                print '\n \t \t \t \t \t \t \t \t \t \t \t   Jogador vencedor:', self._jogadorVencedor
                print '\t \t \t \t \t \t \t \t \t ##############################################################'
                break

            if not self._posicoesDisponiveis:
                print '\n \t \t \t \t \t \t \t \t \t \t \t   Jogo terminou empatado.'
                print '\t \t \t \t \t \t \t \t \t ##############################################################'
                break

        stop = raw_input("Jogar novamente? y/n:")

        if stop == 'y':
            Ligue4(self._jogador, self._modo).run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emula o jogo Ligue4 (Jogador vs IA). Foi utilizado o algoritmo Minimax com poda alfa e beta para implementação das jogadas da IA.')
    parser.add_argument('nome', type=str, help="Nome do jogador que disputará contra a IA.")
    parser.add_argument('-modo', type=str, choices=list(('facil', 'normal', 'dificil')), help="Um modo de dificuldade do jogo.")

    args = parser.parse_args()

    Ligue4(args.nome, args.modo).run()
