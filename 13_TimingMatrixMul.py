"""
CS3C, Assignment #3, Timing Matrix Multiplication
Ulises Marian
"""

from assignment02_instructor_solution import *
import numpy as np
import random
import time
import matplotlib.pyplot as plt

def mulmat(a, b):
    # This function returns the product of a and b, which is another matrix
    if len(a) != len(b[0]) and len(a[0]) != len(b):
        raise IndexError
    matrix_product = []
    for row in a:
        row_product = []
        for col in zip(*b):
            row_product.append(sum([i * j for (i, j) in zip(row, col)]))
        matrix_product.append(row_product)
    return matrix_product

class SparseMatrixMul(SparseMatrix):
    def __mul__(self, other):
        if not isinstance(other, SparseMatrix):
            raise TypeError
        sparse_matrix_product = SparseMatrix(self.nrows, other.ncols,
                                        default_value=0)
        for row in range(len(self._rows)):
            for other_col in range(other.ncols):
                product = 0
                #dot product
                for col_index_of_row_a in (range(self.ncols)):
                    value1 = self.get(row, col_index_of_row_a)
                    if value1 == self.default_value:
                        continue
                    value2 = other.get(col_index_of_row_a, other_col)
                    product += value1 * value2
                    #print(product)
                    #row_product.append(product)
                sparse_matrix_product.set(row, other_col, product)
                #sparse_matrix_product.append(row_product)
        return sparse_matrix_product

"""
1. My expected big O of matrix multiplication is O(n^3)
because of the three nested loops whose repetitions
depend on the size (range) of the input lists/matrices.

2. The growth rates of all three (mulmat(), numpy and SparseMatrixMul.__mul__())
are cubic. I wasn't expecting for all three to look so much alike.
They are not exactly cubic, but very close, they all oscillate around a 
cubic growth rate.

3.Numpy is the fastest, mulmat() is the second fastest, and the slowest is
SparseMatrixMul.__mul__().

The order does not surprise me.
I expected numpy to be the fastest because ultimately that's what numpy is for,
for numeric data calculation. So it is faster than Python list, 
and mulmat() is composed of lists of python lists, 
so it was expected that mulmat() would not be as fast as numpy, 
however it was still fast compared to SparseMatrixMul.__mul__().
Regarding SparseMatrixMul.__mul__(), I expected it to be the slowest one
because of the multiple presences of linked lists, in both self and other
(being Sparse Matrix instances). 
Calling .get() on self and other in order to retrieve the matrices' values
 and then calling set() to actually create the product
(a new Sparse Matrix instance) of these, is expected to be a very slow 
operation"""

#scratch_21 for main()
