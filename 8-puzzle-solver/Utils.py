class Utils(object):

    def exibirRelatorio(self, nodoAnalisado):
        nodoPai = nodoAnalisado.nodoPai

        while not nodoPai == None:
            self.exibirEstadoDoNodo(nodoAnalisado)

    def exibirEstadoDoNodo(self, nodoAnalisado):
        j = 1

        tabuleiro = nodoAnalisado.estadoTabuleiro

        for i in (1, 2, 3):
            print('- - - - - - - - - -')
            print('|  ' + str(tabuleiro['a' + str(i) + str(j)]) + '  |  ' + str(tabuleiro['a' + str(i) + str(j + 1)]) + '  |  ' + str(tabuleiro['a' + str(i) + str(j + 2)]) + '  |')
        print('- - - - - - - - - -')