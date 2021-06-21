"""
CS3C, Assignment #9
Recursion limit and pivot selection of Quick sort
Ulises Marian
"""
QS_RECURSION_LIMIT = 15
def quick_sort_x(iterable, start=None, end=None, rec_limit=QS_RECURSION_LIMIT):
    if rec_limit < 2:
        raise ValueError
    def insertion_sort(iterable, start=None, end=None):
        if start is None:
            start = 0
            end = len(iterable)
        for unsorted_index in range(start + 1, end):
            unsorted_data = iterable[unsorted_index]
            k = unsorted_index
            while k > start and iterable[k - 1] > unsorted_data:
                iterable[k] = iterable[k - 1]
                k -= 1
            iterable[k] = unsorted_data

    def partition(iterable, start, end):
        pivot = iterable[start]
        left, right = start + 1, end - 1
        while True:
            while left <= right and iterable[left] <= pivot:
                left += 1
            while left <= right and iterable[right] >= pivot:
                right -= 1
            if left > right:
                break
            iterable[left], iterable[right] = iterable[right], iterable[left]
        iterable[start], iterable[right] = iterable[right], iterable[start]
        return right

    if start is None:
        start = 0
        end = len(iterable)

    if start + rec_limit >= end:
        return insertion_sort(iterable, start, end)

    pivot_index = partition(iterable, start, end)

    quick_sort_x(iterable, start, pivot_index, rec_limit)
    quick_sort_x(iterable, pivot_index + 1, end, rec_limit)



def quick_sort_my_pivot(iterable, start=None, end=None):
    if end is not None and end < 0:
        return
    def partition(iterable, start, end):

        pivot = iterable[end-1]

        left, right = start, end-2
        while True:
            while left <= right and iterable[left] <= pivot:
                # As long as the element is in the smaller partition, keep
                # moving forward
                left += 1
            while left <= right and iterable[right] >= pivot:
                # As long as the element is in the bigger partition, keep
                # moving backward
                right -= 1

            # 'right' has gone to the left of 'left', can stop now
            if left > right:
                break

            # If the two pointers haven't raced passed each other, the elements
            # they point to are in the wrong partition, so swap them
            iterable[left], iterable[right] = iterable[right], iterable[left]

        iterable[end-1], iterable[left] = iterable[left], iterable[end-1]

        return left

    if start is None:
        start = 0
        end = len(iterable)

    if start + 1 >= end:
        # If there's 0 or 1 element in the list, done.
        return

    pivot_index = partition(iterable, start, end)

    quick_sort_my_pivot(iterable, start, pivot_index)
    quick_sort_my_pivot(iterable, pivot_index + 1, end)
    return iterable

""""
As opposed to your implementation of quicksort, which uses the first 
element as the pivot, my implementation does the opposite. It uses the 
last element as the pivot. So the pivot is picked by using "end - 1", 
"end" being the length of the iterable, as the index to the iterable. 
Thus, pivot = iterable[end-1]
"""


def main():
    a = quick_sort_my_pivot([4, 7, 9, 2, 3, 5, 8, 1, 20, 12, 51, 45, 46,
                             47, 33])# 20,
    print(a)

main()


