__author__ = 'Lee'
import Semiring, XSemiring
import math

# really dumb square matrix representation
class Matrix(Semiring.Semiring):
    # flattened list
    # column major
    # 0 3 6
    # 1 4 7
    # 2 5 8
    def __str__(self):
        n = int(math.sqrt(len(self.item)))
        s = ("%s\t"*n) + "\n"
        s = s * n
        l = []
        for i in range(n):
            for j in range(n):
                l.append(self.item[self.idx(i,j)])
        return s%(tuple(l))

    def idx(self, i, j):
        n = int(math.sqrt(len(self.item)))
        return (i + j*n)
    def ij(self, idx):
        n = int(math.sqrt(len(self.item)))
        return (idx % n, idx / n)
    def add(self, right):
        # assume consistency
        new_list = []
        for i in range(len(self.item)):
            new_list.append(self.item[i] + right.item[i])
        return Matrix.lift(new_list)

    def mul(self, right):
        # assume consistency
        n = int(math.sqrt(len(self.item)))
        new_list = []
        # C = AB => c_{ij} = \sum_k a_{ik}b_{kj}
        for j in range(n):
            for i in range(n):
                l = None
                for k in range(n):
                    x = self.item[self.idx(i,k)] * right.item[self.idx(k, j)]
                    if l is None:
                        l = x
                    else:
                        l = l + x
                new_list.append(l)
        return Matrix.lift(new_list)

if __name__ == "__main__":
    A = Matrix([1,2,3,4])
    B = A * A
    print A + A