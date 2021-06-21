"""
CS3C, Assignment #9
Recursion limit and pivot selection of Quick sort
Ulises Marian
"""

from sort_test import SortTestCase
from quicksort import *
from quicksort_test import *
import unittest
from assignment09 import *
import random
import timeit
import matplotlib.pyplot as plt
import sys

class FrameworkTestCase(unittest.TestCase):
    def testRecursionLimitVaryInputSizes(self):
        sys.setrecursionlimit(10 ** 6)
        #print("hello")
        all_durations = []
        for i in range(0,4):
            global recursion_limits
            recursion_limits = []
            global list_of_durations
            list_of_durations = []
            list1 = random.sample(range(1, 1000000), 2000*2**i)
            for j in range(2, 301, 2):
                recursion_limits.append(j)
                self.helpTestPerformance2(list1, j)
            all_durations.append(list_of_durations)

        plt.plot(recursion_limits, all_durations[0])
        plt.plot(recursion_limits, all_durations[1])
        plt.plot(recursion_limits, all_durations[2])
        plt.plot(recursion_limits, all_durations[3])
        plt.xlabel("recursion limit")
        plt.ylabel("duration")
        plt.show()

    sort_func = None
    def helpTestPerformance2(self, sample, recursion_limit):
        global duration
        duration = timeit.timeit(lambda: self.__class__.sort_func(sample,
        None, None, recursion_limit), number=1)
        list_of_durations.append(duration)
        print(f"{self.__class__.sort_func.__name__} on {len(sample)} "
              f"items takes {duration:.6f} seconds "
              f"recursion limit: {recursion_limit}")

class QuickSortXTestCase(FrameworkTestCase):
    sort_func = quick_sort_x

    """"
    quick_sort_x on 2000 items takes 0.014022 seconds recursion limit: 2
    quick_sort_x on 2000 items takes 0.448031 seconds recursion limit: 4
    quick_sort_x on 2000 items takes 0.369637 seconds recursion limit: 6
    quick_sort_x on 2000 items takes 0.359655 seconds recursion limit: 8
    quick_sort_x on 2000 items takes 0.336061 seconds recursion limit: 10
    quick_sort_x on 2000 items takes 0.333429 seconds recursion limit: 12
    quick_sort_x on 2000 items takes 0.315128 seconds recursion limit: 14
    quick_sort_x on 2000 items takes 0.339159 seconds recursion limit: 16
    quick_sort_x on 2000 items takes 0.351934 seconds recursion limit: 18
    quick_sort_x on 2000 items takes 0.295833 seconds recursion limit: 20
    quick_sort_x on 2000 items takes 0.287649 seconds recursion limit: 22
    quick_sort_x on 2000 items takes 0.315366 seconds recursion limit: 24
    quick_sort_x on 2000 items takes 0.335380 seconds recursion limit: 26
    quick_sort_x on 2000 items takes 0.300296 seconds recursion limit: 28
    quick_sort_x on 2000 items takes 0.285346 seconds recursion limit: 30
    
    
    quick_sort_x on 4000 items takes 0.026000 seconds recursion limit: 2
    quick_sort_x on 4000 items takes 1.856041 seconds recursion limit: 4
    quick_sort_x on 4000 items takes 1.691566 seconds recursion limit: 6
    quick_sort_x on 4000 items takes 1.846531 seconds recursion limit: 8
    quick_sort_x on 4000 items takes 3.230522 seconds recursion limit: 10
    quick_sort_x on 4000 items takes 2.227559 seconds recursion limit: 12
    quick_sort_x on 4000 items takes 1.176857 seconds recursion limit: 14
    quick_sort_x on 4000 items takes 1.178567 seconds recursion limit: 16
    quick_sort_x on 4000 items takes 1.315605 seconds recursion limit: 18
    quick_sort_x on 4000 items takes 1.386522 seconds recursion limit: 20
    quick_sort_x on 4000 items takes 1.197950 seconds recursion limit: 22
    quick_sort_x on 4000 items takes 1.319986 seconds recursion limit: 24
    quick_sort_x on 4000 items takes 1.351650 seconds recursion limit: 26
    quick_sort_x on 4000 items takes 1.396023 seconds recursion limit: 28
    quick_sort_x on 4000 items takes 1.181291 seconds recursion limit: 30
    
    
    quick_sort_x on 8000 items takes 0.044446 seconds recursion limit: 2
    quick_sort_x on 8000 items takes 5.857868 seconds recursion limit: 4
    quick_sort_x on 8000 items takes 4.196152 seconds recursion limit: 6
    quick_sort_x on 8000 items takes 4.605022 seconds recursion limit: 8
    quick_sort_x on 8000 items takes 4.050799 seconds recursion limit: 10
    quick_sort_x on 8000 items takes 4.517126 seconds recursion limit: 12
    quick_sort_x on 8000 items takes 5.885068 seconds recursion limit: 14
    quick_sort_x on 8000 items takes 4.972589 seconds recursion limit: 16
    quick_sort_x on 8000 items takes 5.356096 seconds recursion limit: 18
    quick_sort_x on 8000 items takes 4.559787 seconds recursion limit: 20
    quick_sort_x on 8000 items takes 4.261355 seconds recursion limit: 22
    quick_sort_x on 8000 items takes 4.066816 seconds recursion limit: 24
    quick_sort_x on 8000 items takes 4.941486 seconds recursion limit: 26
    quick_sort_x on 8000 items takes 5.566644 seconds recursion limit: 28
    quick_sort_x on 8000 items takes 4.368196 seconds recursion limit: 30
    
    
    quick_sort_x on 16000 items takes 0.078434 seconds recursion limit: 2
    quick_sort_x on 16000 items takes 17.854217 seconds recursion limit: 4
    quick_sort_x on 16000 items takes 15.504138 seconds recursion limit: 6
    quick_sort_x on 16000 items takes 16.986124 seconds recursion limit: 8
    quick_sort_x on 16000 items takes 14.972005 seconds recursion limit: 10
    quick_sort_x on 16000 items takes 16.502158 seconds recursion limit: 12
    quick_sort_x on 16000 items takes 21.167072 seconds recursion limit: 14
    quick_sort_x on 16000 items takes 20.908127 seconds recursion limit: 16
    quick_sort_x on 16000 items takes 16.783925 seconds recursion limit: 18
    quick_sort_x on 16000 items takes 15.733189 seconds recursion limit: 20
    quick_sort_x on 16000 items takes 20.100767 seconds recursion limit: 22
    quick_sort_x on 16000 items takes 21.844120 seconds recursion limit: 24
    quick_sort_x on 16000 items takes 36.970118 seconds recursion limit: 26
    quick_sort_x on 16000 items takes 38.202207 seconds recursion limit: 28
    quick_sort_x on 16000 items takes 33.207141 seconds recursion limit: 30
    
    From my results, I believe the optimal range of rec_limit is 0-20. Although 
    sometimes a bigger rec_limit value seems to perform as fast as a smaller 
    one, that is not strange given that the input data is randomly 
    allocated, therefore the benefit of sorting with a larger rec_limit or a 
    smaller rec_limit comes down to 'how bad' or 'how good' the iterable 
    initially is. An iterable that is almost entirely sorted from the very 
    beginning vs an iterable that is not sorted at all, will affect the 
    performance of the algorithm very differently, even if they have the same 
    rec_limit.
    Nevertheless, in general I believe a range of 0-20 is the optimal option.
    """
#random data
class TestPerformance(SortTestCase):
    sort_func = None

    def testPerformance(self):
        for length in itertools.chain([10, 100, 500], range(1000, 600000,
                                                            10000)):
            sample = random.sample(range(1000000), length)
            self.helpTestPerformance(sample)

    def helpTestPerformance(self, sample):
        duration = timeit.timeit(lambda: self.__class__.sort_func(sample), number=1)
        print(f"{self.__class__.sort_func.__name__} on {len(sample)} "
              f"items takes {duration:.6f} seconds")

#was having trouble using helpTestPerformance from SortTestCase...
# class helpMyPivot(SortTestCase):
#     def callHelpTestPerformance(self):
#         sample = [4, 7, 9, 2, 3, 5, 8, 1]
#         self.helpTestPerformance(sample)

    # sort_func = None

    # def helpTestPerformance(self, sample):
    #     duration = timeit.timeit(lambda: self.__class__.sort_func(sample), number=1)
    #     print(f"{self.__class__.sort_func.__name__} on {len(sample)} "
    #           f"items takes {duration:.6f} seconds")

class QuickSortMyPivot(TestPerformance):
    sort_func = quick_sort_my_pivot

class QuickSortMeasure(TestPerformance):
    sort_func = quick_sort

class QuickSortM3Measure(TestPerformance):
    sort_func = quick_sort_m3

#WORST case

class GenericTest(SortTestCase):  #tried inhering your generic one, but kept
    # getting a NameError
    def testWorstCasePerformance(self):
        # Need higher recursion limit for worst-case scenario for quick-sort
        sys.setrecursionlimit(10 ** 6)
        print("Worst case (for quick sort) performance")
        for length in itertools.chain([10, 100, 500], range(1000, 20000, 2000)):
            sample = list(range(length))
            self.helpTestPerformance(sample)

class QuickSortMyPivot2(GenericTest):
    sort_func = quick_sort_my_pivot

class QuickSortMeasure2(GenericTest):
    sort_func = quick_sort

class QuickSortM3Measure2(GenericTest):
    sort_func = quick_sort_m3

""""
in the worst case, with sorted data, quick_sort_m3() is the fastest 
regardless of the size of the iterable.
It is expected because it samples the input. It finds a pivot that 
splits the input into approximately two equal parts.

Interestingly, for random data, quick_sort_my_pivot is the fastest when the 
iterable is very big. And even more interesting is that quick_sort_m3 is, 
generally, the slowest one. I did not expected that.

Furthermore, in general, quick_sort is the fastest. However, quick_sort_my_pivot
is the fastest in several cases (besides the already mentioned for really big iterables,
whose output you can appreciate below).

quick_sort_my_pivot on 541000 items takes 3.176191 seconds
quick_sort_my_pivot on 551000 items takes 3.059211 seconds
quick_sort_my_pivot on 561000 items takes 3.237955 seconds
quick_sort_my_pivot on 571000 items takes 3.421053 seconds
quick_sort_my_pivot on 581000 items takes 3.357960 seconds
quick_sort_my_pivot on 591000 items takes 3.438533 seconds

quick_sort on 541000 items takes 3.028450 seconds
quick_sort on 551000 items takes 3.251982 seconds
quick_sort on 561000 items takes 3.890491 seconds
quick_sort on 571000 items takes 3.600024 seconds
quick_sort on 581000 items takes 3.401600 seconds
quick_sort on 591000 items takes 3.865203 seconds

quick_sort_m3 on 541000 items takes 3.910335 seconds
quick_sort_m3 on 551000 items takes 3.977419 seconds
quick_sort_m3 on 561000 items takes 4.085832 seconds
quick_sort_m3 on 571000 items takes 4.481702 seconds
quick_sort_m3 on 581000 items takes 4.211176 seconds
quick_sort_m3 on 591000 items takes 4.384456 seconds
"""

