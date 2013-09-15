__author__ = 'Lee'

# a semi ring contains two operations
class Semiring(object):
    def __init__(self, item):
        # lift into this semiring
        self.item = item

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        return str(self)

    @classmethod
    def lift(cls, item):
        if (isinstance(item, Semiring)):
            return cls(item.item)
        return cls(item)

    def mul(self, right):
        pass

    def add(self, right):
        pass

    def __mul__(self, other):
        return self.mul(self.lift(other))

    def __rmul__(self, other):
        return self.lift(other).mul(self)

    def __add__(self, other):
        return self.add(self.lift(other))

    def __radd__(self, other):
        return self.lift(other).add(self)

if __name__ == "__main__":
    class R(Semiring):
        def mul(self, right):
            return R.lift(self.item * right.item)

        def add(self, right):
            return R.lift(self.item + right.item)

    a = R.lift(1)
    b = a.lift(2)
    print a + b * b