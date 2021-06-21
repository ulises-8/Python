"""
CS3C, Assignment #6
A few min heap coding exercises
Ulises Marian
"""

from minheap import *

class MedianHeap(MinHeap):
    def remove(self):
        if len(self) == 0:
            raise IndexError("Remove from empty min heap")

        return_data = self._heap[len(self)//2]
        # Always remove data at the end of the heap first
        last_data = self._heap.pop()
        if len(self) > 0:
            self._heap[1] = last_data
            self._percolate_down(1)

        return return_data

    def insert(self, data):
        self._heap.append(data)
        self.sorting(self._heap)
        self._percolate_up()

    def remove(self):
        if len(self) == 0:
            raise IndexError("Remove from empty median heap")

        self.sorting(self._heap)  #sorts self._heap
        if len(self) % 2 == 0:
            return_data = self._heap[len(self) // 2 + 1]
            saved = self._heap[len(self) // 2 + 1]
            new_last = return_data   #median becomes last elemnt
        else: #heap is odd
            return_data = self._heap[len(self) // 2 + 1]
            #print(return_data, "return")
            saved = self._heap[len(self) // 2 + 1]
        if len(self._heap) == 3:
            new_median = self._heap[len(self) -1]
        else:
            new_median = self._heap[len(self)]
        last_data = self._heap.pop()
        if len(self) > 0:
            if len(self._heap) == 3:
                self._heap[len(self) // 2 +1] = new_median
                saved = last_data
                self._percolate_down(1)
            elif len(self._heap) % 2 == 0:
                try:
                    self._heap[len(self) // 2 + 2] = new_median
                except:
                    self._heap[len(self) // 2 + 1] = new_median
                saved = last_data
                self._percolate_down(1)
            else:  #if len is odd
                self._heap[len(self) // 2+1] = new_median
                saved = last_data
                self._percolate_down(1)
        return return_data

    def sorting(self, heap):
        sorted_heap = []
        for num in heap:
            if num is not None:
                sorted_heap.append(num)
        new_heap = sorted(sorted_heap)
        new_heap.insert(0, None)
        self._heap = new_heap


