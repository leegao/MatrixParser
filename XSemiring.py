__author__ = 'Lee'
import Semiring

Semiring = Semiring.Semiring

class XSemiringFactory(object):
    @classmethod
    def constructor(cls, cnf):
        class XSemiring(Semiring):
            def mul(self, other):
                # join of all left variables of
                s = set([])
                for X in self.item:
                    for Y in other.item:
                        vars = cnf.left_of(X, Y)
                        for V in vars:
                            s.add(V)
                return self.lift(s)

            def add(self, other):
                # join of left and right
                return self.lift((self.item.union(other.item)))

        return XSemiring

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
    print grammar
    print grammar.reverse
    X = XSemiringFactory.constructor(grammar)

    a = X.lift(set(['X']))
    b = X.lift(set(['Y']))
    print a * b