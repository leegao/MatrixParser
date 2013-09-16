__author__ = 'Lee'
import Semiring

Semiring = Semiring.Semiring

class XSemiringFactory(object):
    @classmethod
    def constructor(cls, cnf):
        class XSemiring(Semiring):
            def __str__(self):
                return str(list(self.item))

            def mul(self, other):
                # join of all left variables of
                s = set([])
                for Xx in self.item:
                    for Yy in other.item:
                        vars = cnf.left_of(Xx[0], Yy[0])
                        for V in vars:
                            s.add((V, Xx, Yy))
                return self.lift(s)

            def add(self, other):
                # join of left and right
                return self.lift((self.item.union(other.item)))

        return XSemiring

def dot(tree):
    global idd
    idd = 0
    def __helper__(tree):
        global idd
        id = idd
        idd += 1
        if len(tree) == 1:
            # leaf
            return ('n%s[label="%s"]\n'%(id,tree[0]), id)
        else:
            # binary
            left = __helper__(tree[1])
            right = __helper__(tree[2])

            return ('n%s[label="%s"]\n n%s -> n%s\n n%s -> n%s\n %s %s'%(id, tree[0], id, left[1], id, right[1], left[0], right[0]), id)

    return "digraph {\n" + __helper__(tree)[0] + "}"

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

    a = X.lift({('X', ('A', 'a'), ('A', 'a'))})
    b = X.lift({('Y', ('B', 'b'), ('B', 'b'))})
    print a * b