from Nodo import Nodo
from Heuristica import Heuristica
from Utils import Utils
from EightPuzzleSolver import EightPuzzleSolver

estadoTabuleiro = {'a11': 2, 'a12': ' ', 'a13': 3, 
				   'a21': 4, 'a22': 8, 'a23': 6,
				   'a31': 1, 'a32': 5, 'a33': 7}

nodoInicial = Nodo(estadoTabuleiro, 0, 0, None)
EightPuzzleSolver = EightPuzzleSolver()
EightPuzzleSolver.AStarAlgorithm(nodoInicial, True)
