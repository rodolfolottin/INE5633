from Nodo import Nodo
from Heuristica import Heuristica
from Utils import Utils
from EightPuzzleSolver import EightPuzzleSolver

estadoTabuleiro = {'a11': 2, 'a12': 3, 'a13': 6,
				   'a21': 4, 'a22': 5, 'a23': 8,
				   'a31': ' ', 'a32': 1, 'a33': 7}

estadoTabuleiro2 = {'a11': 6, 'a12': 5, 'a13': 3,
                   'a21': 4, 'a22': 7, 'a23': 1,
                   'a31': 2, 'a32': 8, 'a33': ' '}

estadoTabuleiro3 = {'a11': 3, 'a12': 8, 'a13': 6,
                   'a21': 1, 'a22': ' ', 'a23': 5,
                   'a31': 2, 'a32': 7, 'a33': 4}

nodoInicial = Nodo(estadoTabuleiro3, 0, 0, None)
EightPuzzleSolver = EightPuzzleSolver()
EightPuzzleSolver.AStarAlgorithm(nodoInicial, True)
