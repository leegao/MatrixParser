__author__ = 'Lee'

import Semiring, XSemiring, MatrixRing

def initial_matrix(cnf, words):
    X = XSemiring.XSemiringFactory.constructor(cnf)
    n = len(words) + 1
    f = lambda i,j: X.lift(set([])) if i != j + 1 else X.lift({(cnf.term_of(words[j]),)})
    return MatrixRing.Matrix.lift([f(i,j) for i in range(n) for j in range(n)])

if __name__ == "__main__":
    import CNF, math
    Grammar = CNF.Grammar

    grammar = Grammar()
    grammar.add_term('(', '(')
    grammar.add_term(')', ')')
    grammar.add_bin('X', '(', 'A')
    grammar.add_bin('A', 'X', ')')
    grammar.add_bin('A', 'A', 'A')
    grammar.add_bin('A', '(', ')')

    A = initial_matrix(grammar, "((()())())")
    #print A
    P = A
    n = int(math.sqrt(len(A.item)))
    for i in range(int(math.sqrt(len(A.item)))):
        P = P + P*P
        #print P.item[P.idx(0,n-1)]

    for tree in P.item[P.idx(0,n-1)].item:
        print XSemiring.dot(tree)

