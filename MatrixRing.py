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
            new_list.append(self.item * right.item)
        return Matrix.lift(new_list)

    def mul(self, right):
        # assume consistency
        n = int(math.sqrt(len(self.item)))
        new_list = []
        # C = AB => c_{ij} = \sum_k a_{ik}b_{kj}
        for i in range(n):
            for j in range(n):
                l = []
                for k in range(n):
                    l.append(self.item[self.idx(i,k)] * self.item[self.idx(k, j)])
                new_list.append(sum(l))
        return Matrix.lift(new_list)