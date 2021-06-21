"""
CS3C, Assignment #6
A few min heap coding exercises
Ulises Marian
"""

from assignment06 import *
from minheap_test import *
from minheap import *
import unittest
import random
import time

class MoreMinHeapTestCase(unittest.TestCase):
    def assertIsMinHeap(self, minheap):
        if minheap is not None:
            self.assertIsInstance(minheap, MinHeap)
            self.assertEqual(len(minheap), len(minheap._heap)-1)
            for i in range(len(minheap._heap)):
                if minheap._heap[i] is None:
                    continue
                if len(minheap._heap) > i*2:   #checking if first child (left)
                    self.assertLessEqual(minheap._heap[i], minheap._heap[i * 2])

                if len(minheap._heap) > i*2+1: #checking if second child (right)
                    self.assertLessEqual(minheap._heap[i],
                                         minheap._heap[i * 2 + 1])

    def testIsMinHeap(self):
        heap = MinHeap([10, 4, 8, 12, 30, 17])
        self.assertIsMinHeap(heap)

    def testInsertRemoveRandom(self):
        heap = MinHeap()
        data = random.sample(range(1, 1200), 1100)
        for num in data:
            heap.insert(num)
            self.assertIsMinHeap(heap)
        self.helperRemove(heap)

    def helperRemove(self, heap):
        print(f"heap: {heap}")
        new_list = []
        for num in heap._heap:
            if num is None:
                continue
            new_list.append(num)
        sorted_list = sorted(new_list, reverse=True)
        for _ in range(len(sorted_list)):
            removed_min = heap.remove()
            removed_last = sorted_list.pop()
            if len(heap._heap) > 1:
                self.assertEqual(removed_last, removed_min)
                self.assertIsMinHeap(heap)
        print(f"heap: {heap}")

    def testFloydVsWilliam(self):
        print("worst cases...")
        self.worstCaseFloyd4()
        self.worstCaseWilliam4()
        print()
        self.worstCaseFloyd()
        self.worstCaseWilliam()
        print()
        self.worstCaseFloyd2()
        self.worstCaseWilliam2()
        print()
        self.worstCaseFloyd3()
        self.worstCaseWilliam3()
        print()

        #average cases
        print("average cases...")
        self.averageCaseFloyd()
        self.averageCaseWilliam()
        print()
        self.averageCaseFloyd2()
        self.averageCaseWilliam2()
        print()
        self.averageCaseFloyd3()
        self.averageCaseWilliam3()
        print()
        self.averageCaseFloyd4()
        self.averageCaseWilliam4()

    # 10 nodes
    def worstCaseFloyd(self):
        #worst case
        start = time.perf_counter()
        floyd_heap = MinHeap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        print(floyd_heap)
        duration = time.perf_counter() - start
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def worstCaseWilliam(self):
        start = time.perf_counter()
        william_heap = MinHeap()
        for i in range(10, 0, -1):
            william_heap.insert(i)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")

    #20 nodes
    def worstCaseFloyd2(self):
        start = time.perf_counter()
        floyd_heap = MinHeap([i for i in range(20, 0, -1)])
        duration = time.perf_counter() - start
        print(floyd_heap)
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def worstCaseWilliam2(self):
        start = time.perf_counter()
        william_heap = MinHeap()
        for i in range(20, 0, -1):
            william_heap.insert(i)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")

    #100 nodes
    def worstCaseFloyd3(self):
        start = time.perf_counter()
        floyd_heap = MinHeap([i for i in range(100, 0, -1)])
        duration = time.perf_counter() - start
        print(floyd_heap)
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def worstCaseWilliam3(self):
        start = time.perf_counter()
        william_heap = MinHeap()
        for i in range(100, 0, -1):
            william_heap.insert(i)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")

    #5 nodes
    def worstCaseFloyd4(self):
        start = time.perf_counter()
        floyd_heap = MinHeap([i for i in range(5, 0, -1)])
        duration = time.perf_counter() - start
        print(floyd_heap)
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def worstCaseWilliam4(self):
        start = time.perf_counter()
        william_heap = MinHeap()
        for i in range(5, 0, -1):
            william_heap.insert(i)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")


    def averageCaseFloyd(self):
        #average case
        start = time.perf_counter()
        floyd_heap = MinHeap([4, 30, 29, 28, 27, 26, 24])
        duration = time.perf_counter() - start
        print(floyd_heap)
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def averageCaseWilliam(self):
        list_ = [4, 30, 29, 28, 27, 26, 24]
        start = time.perf_counter()
        william_heap = MinHeap()
        for num in list_:
            william_heap.insert(num)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")

    def averageCaseFloyd2(self):
        # average case
        start = time.perf_counter()
        floyd_heap = MinHeap([4, 30, 29, 28, 27, 26, 24, 17, 16, 20, 14, 23,
                              21, 12, 10, 19, 32, 15, 9, 22, 11])
        duration = time.perf_counter() - start
        print(floyd_heap)
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def averageCaseWilliam2(self):
        list_ = [4, 30, 29, 28, 27, 26, 24, 17, 16, 20, 14, 23,
                              21, 12, 10, 19, 32, 15, 9, 22, 11]
        start = time.perf_counter()
        william_heap = MinHeap()
        for num in list_:
            william_heap.insert(num)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")

    def averageCaseFloyd3(self):
        # average case
        start = time.perf_counter()
        floyd_heap = MinHeap([4, 30, 29, 28, 27, 26, 24, 17, 16, 20, 14, 23,
                              21, 12, 10, 19, 32, 15, 9, 22, 11, 60, 55, 13,
                              39, 6, 36, 25, 63, 100, 31, 64, 50, 7, 18, 44,
                              25, 49, 34, 43, 42, 71, 92, 76, 53, 66, 33, 47,
                              20, 58, 88, 69, 77, 98, 81, 65, 84, 72, 59, 91,
                              96, 82, 89, 61, 43, 86, 37, 110, 107, 200, 150,
                              8, 113])
        duration = time.perf_counter() - start
        print(floyd_heap)
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def averageCaseWilliam3(self):
        list_ = [4, 30, 29, 28, 27, 26, 24, 17, 16, 20, 14, 23,
                 21, 12, 10, 19, 32, 15, 9, 22, 11, 60, 55, 13,
                 39, 6, 36, 25, 63, 100, 31, 64, 50, 7, 18, 44,
                 25, 49, 34, 43, 42, 71, 92, 76, 53, 66, 33, 47,
                 20, 58, 88, 69, 77, 98, 81, 65, 84, 72, 59, 91,
                 96, 82, 89, 61, 43, 86, 37, 110, 107, 200, 150,
                 8, 113]
        start = time.perf_counter()
        william_heap = MinHeap()
        for num in list_:
            william_heap.insert(num)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")

    def averageCaseFloyd4(self):
        # average case
        start = time.perf_counter()
        floyd_heap = MinHeap([4, 30, 29, 28, 27, 26, 24, 17, 16, 20, 14, 23,
                              21, 12, 10, 19, 32, 15, 9, 22, 11, 60, 55, 13,
                              39, 6, 36, 25, 63, 100, 31, 64, 50, 7, 18, 44,
                              25, 49, 34, 43, 42, 71, 92, 76, 53, 66, 33, 47,
                              20, 58, 88, 69, 77, 98, 81, 65, 84, 72, 59, 91,
                              96, 82, 89, 61, 43, 86, 37, 110, 107, 200, 150,
                              8, 113, 105, 133, 143, 116, 122, 148, 172, 184,
                              250, 260, 221, 220, 204, 112, 113, 119, 83,
                              111, 174, 190, 182, 151, 131, 142, 106, 92, 82,
                              34, 87, 40, 39, 161, 59])
        duration = time.perf_counter() - start
        print(floyd_heap)
        print("floyd's duration", duration)
        print(f"percolate down # of movements: "
              f"{floyd_heap.percolate_down_count}")

    def averageCaseWilliam4(self):
        list_ = [4, 30, 29, 28, 27, 26, 24, 17, 16, 20, 14, 23,
                 21, 12, 10, 19, 32, 15, 9, 22, 11, 60, 55, 13,
                 39, 6, 36, 25, 63, 100, 31, 64, 50, 7, 18, 44,
                 25, 49, 34, 43, 42, 71, 92, 76, 53, 66, 33, 47,
                 20, 58, 88, 69, 77, 98, 81, 65, 84, 72, 59, 91,
                 96, 82, 89, 61, 43, 86, 37, 110, 107, 200, 150,
                 8, 113, 105, 133, 143, 116, 122, 148, 172, 184,
                 250, 260, 221, 220, 204, 112, 113, 119, 83,
                 111, 174, 190, 182, 151, 131, 142, 106, 92, 82,
                 34, 87, 40, 39, 161, 59]
        start = time.perf_counter()
        william_heap = MinHeap()
        for num in list_:
            william_heap.insert(num)
        duration = time.perf_counter() - start
        print("williams duration", duration)
        print(f"percolate up # of movements: "
              f"{william_heap.percolate_up_count}")

    """"
    For the worst case, these are my findings:
    The William's method does require more movements than Floyd's, in all 
    cases. However, despite the larger amount of movements by William's, 
    it was sometimes faster in 3/4 of the test cases, sometimes it was 
    divided 2/4, for each, William's and Floyd's. All the test cases varied, 
    sometimes they would go to William, sometimes to Floyd. That I did not 
    expect.
    
    Interestingly, the second case (which has more nodes and makes more movements
    than the first case) is sometimes faster (sometimes just the William's, 
    some other times just the Floyd's, and sometimes both) than the first case.
    
    For the average cases, the findings were similar to the worst cases, 
    where despite the William's had more movements in all the cases, 
    they were sometimes faster in 2/4, or 3/4, and even 4/4 cases. Leaving 
    aside this surprise, I'm amazed by how fast the William's method is 
    despite doing 2x or even 4-5x the amount of movements as Floyd. On the 
    other hand, being able to do the work in very little moves is also an 
    amazing feat, so I think both are very interesting 'methods'
    """

class MedianHeapTestCase(unittest.TestCase):
    def testInsertMedian(self):
        medianheap = MedianHeap()
        data = [5, 9, 3, 7, 1]
        for d in data:
            medianheap.insert(d)
        expected = [None, 1, 3, 5, 7, 9]
        self.assertListEqual(expected, medianheap._heap)
        self.assertEqual(len(medianheap), len(data))

    def testRemove(self):
        medianheap = MedianHeap()
        data = [5, 7, 3, 9, 1, 12, 8]
        for d in data:
            medianheap.insert(d)

        expected = 7
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 8
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 5
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 9
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 3
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 12
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 1
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = [None]
        actual = medianheap._heap
        self.assertEqual(expected, actual)

    def testRemove2(self):
        medianheap = MedianHeap()
        data = [10, 20, 30, 5, 12, 16, 40, 33, 70, 64]
        for d in data:
            medianheap.insert(d)

        expected = 30
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 20
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 33
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 16
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 40
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 12
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 64
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 10
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = 70
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = [None, 5]
        actual = medianheap._heap
        self.assertEqual(expected, actual)

        expected = 5
        actual = medianheap.remove()
        self.assertEqual(expected, actual)

        expected = [None]
        actual = medianheap._heap
        self.assertEqual(expected, actual)

    def testInitWithData(self):
        data = [5, 9, 3, 7, 1, 12, 8]
        medianheap = MedianHeap(data)
        expected = [None, 1, 5, 3, 7, 9, 12, 8]
        self.assertListEqual(expected, medianheap._heap)
        self.assertEqual(len(data), len(medianheap))

    def testInitWithData2(self):
        data = [15, 9, 3, 7, 1]
        medianheap = MedianHeap(data)
        expected = [None, 1, 7, 3, 15, 9]
        self.assertListEqual(expected, medianheap._heap)
        self.assertEqual(len(data), len(medianheap))

