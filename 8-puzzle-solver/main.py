from Nodo import Nodo
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

estadoTabuleiro4 = {'a11': 6, 'a12': 5, 'a13': 3,
                    'a21': 4, 'a22': 7, 'a23': 1,
                    'a31': ' ', 'a32': 2, 'a33': 8}

piorCasoPossivel = {'a11': 5, 'a12': 8, 'a13': 7,
                                        'a21': 1, 'a22': ' ', 'a23': 6,
                                        'a31': 3, 'a32': 2, 'a33': 4}

_nodo_objetivo = {'a11': 1, 'a12': 2, 'a13': 3,
                  'a21': 8, 'a22': ' ', 'a23': 4,
                  'a31': 7, 'a32': 6, 'a33': 5}

nodoInicial = Nodo(piorCasoPossivel, 0, 0, None)
EightPuzzleSolver = EightPuzzleSolver()
EightPuzzleSolver.AStarAlgorithm(nodoInicial, True)
