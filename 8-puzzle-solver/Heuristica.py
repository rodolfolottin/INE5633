import math

class Heuristica(object):

    @staticmethod
    def numeroDePecasForaDoLugar(nodo, nodoObjetivo):
        numPecasHeuristic = 9

        for chave, valor in nodo.viewitems() & nodoObjetivo.viewitems():
            numPecasHeuristic = numPecasHeuristic - 1

        return numPecasHeuristic

    @staticmethod
    def distanciaDeManhattan(nodo, nodoObjetivo):
        LINHA = 1
        COLUNA = 2
        chavesDicionario = ['a11', 'a12', 'a13', 'a21', 'a22', 'a23', 'a31', 'a32', 'a33']

        manhattanHeuristic = 0
        # swap chave e valor dict
        swap_nodo_objetivo = dict((v,k) for k,v in nodoObjetivo.iteritems())

        for chave in chavesDicionario:
            if nodo[chave] != nodoObjetivo[chave]:
                pecaObjtv = swap_nodo_objetivo[nodo[chave]]
                # conversoes pois a chave ('aij') vem como string
                linha = int(chave[LINHA])
                coluna = int(chave[COLUNA])
                distParaPosicaoCorreta = int(math.fabs(int(pecaObjtv[LINHA]) - linha)) +int(math.fabs(int(pecaObjtv[COLUNA]) - coluna))
                manhattanHeuristic = manhattanHeuristic + distParaPosicaoCorreta

        return manhattanHeuristic