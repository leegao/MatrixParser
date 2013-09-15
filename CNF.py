__author__ = 'Lee'

class Production(object):
    pass

class Binary(Production):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return self.left + " " + self.right

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Binary):
            return self.left == other.left and self.right == other.left
        return False

class Terminal(Production):
    def __init__(self, leaf):
        self.leaf = leaf

    def __str__(self):
        return self.leaf

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Terminal):
            return other.leaf == self.leaf
        return False

# cnf is a list of var -> production
# we want to be able to reverse this process easily
class Grammar(dict):
    def __init__(self):
        super(Grammar, self).__init__()
        self.reverse = {}
        self.terms = {}

    def init_var(self, var):
        if not (var in self):
            self[var] = []

    def add_term(self, var, leaf):
        self.init_var(var)
        self[var].append(Terminal(leaf))
        if not (leaf in self.terms):
            self.terms[leaf] = set([])
        self.terms[leaf].add(var)

    def add_bin(self, var, left, right):
        self.init_var(var)
        self[var].append(Binary(left, right))
        # update reverse
        # reverse[left][right] = var
        if not (left in self.reverse):
            self.reverse[left] = {}

        if not (right in self.reverse[left]):
            self.reverse[left][right] = set([])

        self.reverse[left][right].add(var)

    def left_of(self, left, right):
        try:
            return self.reverse[left][right] or set([])
        except:
            return set([])

if __name__ == "__main__":
    '''
S -> XY
X -> XA | AA
Y -> Y B | BB
A -> a
B -> b
    '''
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
