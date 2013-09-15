__author__ = 'Lee'

import Semiring, XSemiring, MatrixRing

def initial_matrix(cnf, words):
    X = XSemiring.XSemiringFactory.constructor(cnf)
    n = len(words) + 1
    f = lambda i,j: X.lift(set([])) if i != j + 1 else X.lift(set(cnf.term_of(words[j])))
    return MatrixRing.Matrix.lift([f(i,j) for i in range(n) for j in range(n)])

if __name__ == "__main__":
    import CNF
    Grammar = CNF.Grammar

    grammar = Grammar()
    grammar.add_term('A', 'a')
    grammar.add_term('B', 'b')
    grammar.add_bin('S', 'X', 'Y')
    grammar.add_bin('X', 'X', 'A')
    grammar.add_bin('X', 'A', 'A')
    grammar.add_bin('Y', 'Y', 'B')
    grammar.add_bin('Y', 'B', 'B')

    A = initial_matrix(grammar, "aabb")
    P = A
    print P
    P = P + P * P
    print P
    P = P + P * P
    print P

