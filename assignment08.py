"""
CS3C, Assignment #8
Analyzing Shellsort's Gaps
Ulises Marian
"""
from sort import *


def shells_gaps_explicit(length):
    gap_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096,
                8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]

    if length < 2:
        return
    for gap in range(len(gap_list) -1, -1, -1):
        if gap_list[gap] < length:
            yield gap_list[gap]

# Had initially implemented it with a while loop, and unncessary* calculations
# def shells_gaps_explicit(length):
#     gap_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096,
#                 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
#     if length < 2:
#         return
#     for gap in gap_list:
#         if gap >= length:
#             yield gap//2
#             gap//=2
#             while gap > 0:
#                 if gap < 2:
#                     break
#                 yield gap//2
#                 gap//=2
#             break


def shell_sort_explicit(iterable):
    return shell_sort(iterable, gaps=shells_gaps_explicit)


def sedgewick_gaps(length):
    if length < 2:
        return
    k = 1
    result = (4**k + (3 * (2**(k - 1)))) + 1
    gaps = [1]
    while result < length:
        gaps.append(result)
        k += 1
        result = (4 ** k + (3 * (2 ** (k - 1)))) + 1
    for i in range(len(gaps)):
        yield gaps[k - 1]
        k -= 1

def shell_sort_sedgewick(iterable):
    return shell_sort(iterable, gaps=sedgewick_gaps)


def my_gaps(length):
    if length < 2:
        return
    k = 1
    result = (2 ** k + (2 * (3 ** (k - 1)))) + 1
    gaps = [1]
    while result < length:
        gaps.append(result)
        k += 1
        result = (2 ** k + (2 * (3 ** (k - 1)))) + 1
    for i in range(len(gaps)):
        yield gaps[k - 1]
        k -= 1

def shell_sort_my(iterable):
    return shell_sort(iterable, gaps=my_gaps)