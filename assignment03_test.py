"""
CS3C, Assignment #3, Timing Matrix Multiplication
Tests
Ulises Marian
"""

from assignment03 import *
import unittest
import random
import numpy as np
import time
import matplotlib.pyplot as plt

class SparseMatrixMulTestCase(unittest.TestCase):
    # 4x4 SparseMatrixMul.__mul__()
    def testMultSquareMatrices(self):
        matrix1 = SparseMatrix(4, 4, 0)
        matrix1.set(0, 0, 13)
        matrix1.set(0, 1, 9)
        matrix1.set(0, 2, 7)
        matrix1.set(0, 3, 15)
        matrix1.set(1, 0, 8)
        matrix1.set(1, 1, 7)
        matrix1.set(1, 2, 4)
        matrix1.set(1, 3, 6)
        matrix1.set(2, 0, 6)
        matrix1.set(2, 1, 4)
        matrix1.set(2, 2, 0)
        matrix1.set(2, 3, 3)
        matrix1.set(3, 0, 1)
        matrix1.set(3, 1, 2)
        matrix1.set(3, 2, 3)
        matrix1.set(3, 3, 8)

        matrix2 = SparseMatrix(4, 4, 0)
        matrix2.set(0, 0, 5)
        matrix2.set(0, 1, 4)
        matrix2.set(0, 2, 7)
        matrix2.set(0, 3, 3)
        matrix2.set(1, 0, 5)
        matrix2.set(1, 1, 3)
        matrix2.set(1, 2, 9)
        matrix2.set(1, 3, 6)
        matrix2.set(2, 0, 9)
        matrix2.set(2, 1, 4)
        matrix2.set(2, 2, 2)
        matrix2.set(2, 3, 3)
        matrix2.set(3, 0, 3)
        matrix2.set(3, 1, 8)
        matrix2.set(3, 2, 8)
        matrix2.set(3, 3, 9)

        #expected product matrix
        product = SparseMatrix(4, 4, 0)
        product.set(0, 0, 218)
        product.set(0, 1, 227)
        product.set(0, 2, 306)
        product.set(0, 3, 249)
        product.set(1, 0, 129)
        product.set(1, 1, 117)
        product.set(1, 2, 175)
        product.set(1, 3, 132)
        product.set(2, 0, 59)
        product.set(2, 1, 60)
        product.set(2, 2, 102)
        product.set(2, 3, 69)
        product.set(3, 0, 66)
        product.set(3, 1, 86)
        product.set(3, 2, 95)
        product.set(3, 3, 96)

        expected = str(product)
        actual = str(SparseMatrixMul.__mul__(matrix1, matrix2))
        self.assertEqual(expected, actual)

    # 4x4 mulmat()
    def testMulMatSquareMatrices(self):
        matrix1 = [[13, 9, 7, 15],
                   [8, 7, 4, 6],
                   [6, 4, 0, 3],
                   [1, 2, 3, 8]]

        matrix2 = [[5, 4, 7, 3],
                   [5, 3, 9, 6],
                   [9, 4, 2, 3],
                   [3, 8, 8, 9]]

        expected = [[218, 227, 306, 249], [129, 117, 175, 132],
                    [59, 60, 102, 69], [66, 86, 95, 96]]

        actual = mulmat(matrix1, matrix2)
        self.assertEqual(expected, actual)

    # 2x3 3x2 SparseMatrixMul.__mul__()
    def testMultRectangularMatrices(self):
        matrix1 = SparseMatrix(2, 3, 0)
        matrix2 = SparseMatrix(3, 2, 0)
        matrix1.set(0, 0, 1)
        matrix1.set(0, 1, 2)
        matrix1.set(0, 2, 3)
        matrix1.set(1, 0, 4)
        matrix1.set(1, 1, 5)
        matrix1.set(1, 2, 6)
        matrix2.set(0, 0, 7)
        matrix2.set(0, 1, 8)
        matrix2.set(1, 0, 9)
        matrix2.set(1, 1, 10)
        matrix2.set(2, 0, 11)
        matrix2.set(2, 1, 12)

        #create expected matrix product
        product = SparseMatrix(2, 2, 0)
        product.set(0,0, 58)
        product.set(0, 1, 64)
        product.set(1, 0, 139)
        product.set(1, 1, 154)

        expected = str(product)
        actual = str(SparseMatrixMul.__mul__(matrix1, matrix2))
        self.assertEqual(expected, actual)

    #2x3 3x2 mulmat()
    def testMulMatRectangularMatrices(self):
        matrix1 = [[1, 2, 3],
                   [4, 5, 6]]

        matrix2 = [[7, 8],
                   [9, 10],
                   [11, 12]]

        expected = [[58, 64], [139, 154]]
        actual = mulmat(matrix1, matrix2)
        self.assertEqual(expected, actual)

    # 10x10 mulmat() vs numpy 10x10
    def testTenbyTenMulMat(self):
        random_matrix1 = [[] for i in range(10)]
        sparse1 = SparseMatrix(10,10,0)
        random.seed(0)
        for row in range(10):
            for col in range(10):
                n = random.randint(0, 100)
                random_matrix1[row].append(n)
                sparse1.set(row, col, n)

        random_matrix2 = [[] for i in range(10)]
        sparse2 = SparseMatrix(10,10,0)
        random.seed(1)
        for row in range(10):
            for col in range(10):
                n = random.randint(0, 100)
                random_matrix2[row].append(n)
                sparse2.set(row, col, n)

        np1 = np.array(random_matrix1)
        np2 = np.array(random_matrix2)
        np_product = np1.dot(np2)
        mulmat_product = mulmat(random_matrix1, random_matrix2)
        expected = mulmat_product
        actual = np_product.tolist()  #convert np result to list
        self.assertEqual(expected, actual)

    # 10x10 SparseMatrixMul.__mul__() vs np 10x10
    def testSparceMatrixTenbyTen(self):
        random_matrix1 = [[] for i in range(10)]
        random.seed(0)
        for row in range(10):
            for col in range(10):
                n = random.randint(0, 100)
                random_matrix1[row].append(n)

        random_matrix2 = [[] for i in range(10)]
        random.seed(1)
        for row in range(10):
            for col in range(10):
                n = random.randint(0, 100)
                random_matrix2[row].append(n)

        sparse10 = SparseMatrix(10, 10, 0)
        random.seed(0)
        for row in range(10):
            for col in range(10):
                n = random.randint(0, 100)
                sparse10.set(row, col, n)

        sparse20 = SparseMatrix(10, 10, 0)
        random.seed(1)
        for row in range(10):
            for col in range(10):
                n = random.randint(0, 100)
                sparse20.set(row, col, n)

        np1 = np.array(random_matrix1)
        np2 = np.array(random_matrix2)
        np_product = np1.dot(np2)
        actual = SparseMatrixMul.__mul__(sparse10, sparse20)

        def sparse_matrix_values(list_, matrix):
            result_matrix = []
            for row in range(len(list_)):
                for col in range(len(list_)):
                    if list_[row][col] == matrix.get(row, col):
                        result_matrix.append(matrix.get(row, col))
            return result_matrix

        sparse_matrix_product = sparse_matrix_values(np_product, actual)

        def np_values(list_, matrix):
            result_list = []
            for row in range(len(list_)):
                for col in range(len(list_)):
                    if list_[row][col] == matrix.get(row, col):
                        result_list.append(list_[row][col])
            return result_list

        np_product = np_values(np_product, actual)
        self.assertEqual(sparse_matrix_product, np_product)

class PerformanceTestCase(unittest.TestCase):
    def MulMatPerformanceMeasurement():
        sizes = [n for n in range(10, 201, 10)]
        x = []
        y = []
        for size in sizes:
            matrix1 = [[] for i in range(size)]
            matrix2 = [[] for i in range(size)]
            for row in range(size):
                for col in range(size):
                    n = random.randint(0, 100)
                    m = random.randint(0, 100)
                    matrix1[row].append(n)
                    matrix2[row].append(m)
            start = time.perf_counter()
            mulmat(matrix1, matrix2)
            duration = time.perf_counter() - start
            print(f"size={size}, duration={duration: .08f}")
            x.append(size)
            y.append(duration)
        plt.plot(x, y)
        plt.xlabel("size")
        plt.ylabel("duration")
        plt.show()
    MulMatPerformanceMeasurement()

    #testing numpy matrix multiplication
    def testNpPerformance():
        sizes = [n for n in range(10, 401, 10)]
        x = []
        y = []
        for size in sizes:
            npy_matrix1 = np.random.randint(100, size=(size, size))
            npy_matrix2 = np.random.randint(100, size=(size, size))
            start = time.perf_counter()
            npy_matrix1.dot(npy_matrix2)
            duration = time.perf_counter() - start
            x.append(size)
            y.append(duration)
            print(f"size={size}, duration={duration: .08f}")
        plt.plot(x, y)
        plt.xlabel("size")
        plt.ylabel("duration")
        plt.show()

    testNpPerformance()

    #SparseMatrixMul.__mul__()
    def testSparceMatrixPerformance():
        sizes = [n for n in range(10, 201, 10)]
        x = []
        y = []
        for size in sizes:
            sparse1 = SparseMatrix(size, size, 0)
            sparse2 = SparseMatrix(size, size, 0)
            for row in range(size):
                for col in range(2):
                    n = random.randint(0, 100)
                    m = random.randint(0, 100)
                    sparse1.set(row, col, n)
                    sparse2.set(row, col, m)
            start = time.perf_counter()
            SparseMatrixMul.__mul__(sparse1, sparse2)
            duration = time.perf_counter() - start
            x.append(size)
            y.append(duration)
            print(f"size={size}, duration={duration: .08f}")
        plt.plot(x, y)
        plt.xlabel("size")
        plt.ylabel("duration")
        plt.show()

    testSparceMatrixPerformance()


