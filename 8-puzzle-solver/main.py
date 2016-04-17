from Nodo import Nodo
from Heuristica import Heuristica
from Utils import Utils
from EightPuzzleSolver import EightPuzzleSolver

estadoTabuleiro = {'a11': 1, 'a12': 2, 'a13': 3, 'a23': 4, 'a33': 5, 'a32': 6, 'a31': 7, 'a21': ' ', 'a22': 8}
nodoInicial = Nodo(estadoTabuleiro, 0, 0, None)
EightPuzzleSolver = EightPuzzleSolver()
EightPuzzleSolver.AStarAlgorithm(nodoInicial, True)