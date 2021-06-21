"""
CS3C, Assignment #8
Analyzing Shellsort's Gaps
Ulises Marian
"""

from sort import *
import unittest
import random
import timeit
import itertools
from sort_test import SortTestCase
from assignment08 import *

class TestPerformance(SortTestCase):
    sort_func = shell_sort

    def testPerformance(self):
        for length in itertools.chain([10, 100, 500], range(1000, 300000,
                                                            10000)):
            sample = random.sample(range(1000000), length)
            self.helpTestPerformance(sample)

    def helpTestPerformance(self, sample):
        duration = timeit.timeit(lambda: self.__class__.sort_func(sample), number=1)
        print(f"{self.__class__.sort_func.__name__} on {len(sample)} "
              f"items takes {duration:.6f} seconds")

    @unittest.skip
    def testShellSortPerformanceNonPowerOf2(self):
        length = 120
        while length < 200000:
            sample = [1, 99] * (length // 2)
            self.helpTestPerformance(sample)
            length *= 2
    """
    We no longer hit the worst case if the length of the list is not a power 
    of 2, because some elements have been moved/sorted by the time we reach the 
    last insertion sort, where the gap is 1. 
    Thus, by the time the last insertion sort is reached, 
    the elements in the list are closer to their final positions.
    """


class ShellSortExplicitTestCase(TestPerformance):
    sort_func = shell_sort_explicit

    @unittest.skip
    def testExplicitGaps(self):
        length = 65
        print(f"explicit shell's gaps up to {length}")
        for gap in shells_gaps_explicit(length):
            print(gap)

    """"
    The performance is indeed different from the baseline. In fact, 
    it is about three times slower than the baseline.
    I initially thought it was due to the while loop I had in my 
    implementation of the gaps, which I then fixed by coming up with an 
    algorithm that only uses a for loop (and not a for loop + while loop). 
    Nevertheless, I was shocked to see the same results from the new 
    performance test, that is, the duration was still 
    three times slower than the baseline.
    
    I was unable to pinpoint why the hard-coded explicit list has such a 
    negative impact on the speed of the function.
    """

class ShellSortSedgewickTestCase(TestPerformance):
    sort_func = shell_sort_sedgewick

    @unittest.skip
    def testSedgewickGaps(self):
        length = 70000
        for gap in sedgewick_gaps(length):
            print(gap)

    """"
    I am surprised to see that Sedgewick's and Hibbard's performances are 
    almost identical. And even more surprising is that their performance is 
    also in line with the baseline. That is, all three of them, the baseline, 
    Sedgewick's and Hibbard's have very similar performances that it seems 
    like there is no considerable difference among them. Nevertheless, 
    I did notice that Sedgewick's is the fastest of the three, then comes 
    Hibbard's, and then the baseline.
    """

# used above, to compare with Hibbard's
class ShellSortHibbardsTestCase(TestPerformance):
    sort_func = shell_sort_hibbard

class ShellSortMyTestCase(TestPerformance):
    sort_func = shell_sort_my

    """
    After doing several experiments, the best gap sequence I could come up 
    with, was one in which I use Sedgewick's as a reference,
    and perform some modifications to it. In fact, my sequence's performance 
    was so similar to Sedgewick's that it was impossible to conclude which 
    one performs better. 
    
    Following the initial results, I though Sedgewick's performed better, 
    but after noticing several cases (different # of items) where
    my gap sequence performed faster than Sedgewick's,
    I could not reach a conclusion. I definitely think Sedgewick's is better,
    because it would be ridiculous if I just happened to improve his algorithm.
  
    Since between my gap sequence and Sedgewick's there are no conclusive 
    discrepancies, it follows that my gap sequence performs better than the 
    explicit gaps' and Hibbard's, because Sedgewick's performs better than both.
    
    Regarding the baseline, my sequence performs better than it.
    """
