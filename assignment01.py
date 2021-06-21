"""
CS3C, Assignment #1, The Subset-Sum Problem
Ulises Marian
"""

class Subset:
    def __init__(self):
        self._my_set = set()
        self._sum = 0

    def __str__(self):
        return str(self._my_set)

    def add(self, item):
        self._sum += item  #every time we add an item, we + it to sum
        self._my_set.add(item)

    @property
    def sum(self):
        return self._sum

    def __eq__(self, other):
        return self._my_set == other._my_set

    @property
    def my_set(self):
        return self._my_set

    def copy_subset(self):
        new_subset = Subset()
        #new_subset.my_set = self.my_set.copy() #alternative
        for i in self.my_set:
            new_subset.add(i)
        return new_subset


class Collection:
    def __init__(self):
        self.list_of_subsets = [Subset()]
        self._max_subset = Subset()

    def __str__(self):
        s = "["
        for subset in self.list_of_subsets:
            s += str(subset)
        s += "]"
        return s

    def expand_by(self, item, target):
        saving_subsets = []
        for subset in self.list_of_subsets:
            if subset.sum == target:
                return subset
            subset = subset.copy_subset()
            if (subset.sum + item) <= target:
                subset.add(item)  #add returns None, so just do mutation
                saving_subsets.append(subset)  #..and append in a differnt line
            elif subset.sum + item == target:
                return  subset
        self.list_of_subsets += saving_subsets
        return None

    @property
    def max_subset(self):
        #return instance of subset in the Collection that has the largest sum
        largest_subset = Subset()
        sum_of_largest_subset = 0
        for subset in self.list_of_subsets:
            if subset.sum > sum_of_largest_subset:
                largest_subset = subset
                sum_of_largest_subset = subset.sum
            self._max_subset = largest_subset
        return self._max_subset


def subset_sum(s, target):
    #initialize col with the empty subset
    check_duplicates = []
    col = Collection()
    matching_subset = 0
    if len(s) == 0:
        return Subset().my_set
    for item in s:
        if item in check_duplicates:
            raise ValueError
        check_duplicates.append(item)
        matching_subset = col.expand_by(item, target)
        try:
            if matching_subset.sum == target:
                return matching_subset.my_set
        except:
            continue
    if matching_subset is None:
        return col.max_subset.my_set
    else:
        return matching_subset


# main - test code
if __name__ == '__main__':
    #empty iterable
    iterable = []
    target = 99
    print(subset_sum(iterable, target))

    #single int iterable
    # target is bigger than int in iterable
    iterable = [8]
    target = 12
    print(subset_sum(iterable, target))

    # target is equal to int in iterable
    iterable = [8]
    target = 8
    print(subset_sum(iterable, target))

    # target is below int in iterable
    iterable = [8]
    target = 4
    print(subset_sum(iterable, target))

    #two ints iterable
    # target is smaller than both ints
    iterable = [33, 34]
    target = 21
    print(subset_sum(iterable, target))

    # target is between the two ints
    iterable = (40, 45)
    target = 43
    print(subset_sum(iterable, target))

    # target is larger than sum of both ints
    iterable = {50, 51}
    target = 102
    print(subset_sum(iterable, target))

    #2+ iterables
    iterable = [33, 34, 70, 5]
    target = 40
    print(subset_sum(iterable, target))

    iterable = (40, 45)
    target = 43
    print(subset_sum(iterable, target))

    # target is smaller than sum of all ints
    iterable = {50, 51, 100, 70, 20, 29}
    target = 301

    # target is larger than all ints
    iterable = {5, 10, 15, 20, 1}
    target = 52
    print(subset_sum(iterable, target))

    # target is equal to sum of all ints
    iterable = [5, 10, 15, 20, 1]
    target = 51
    print(subset_sum(iterable, target))

    # target is less than sum of all ints
    iterable = [5, 10, 15, 20, 1]
    target = 49
    print(subset_sum(iterable, target))

    iterable = [25, 27, 3, 12, 6, 15, 9, 30, 21, 19]
    target = 50
    print(subset_sum(iterable, target))

    iterable = [20, 12, 22, 15, 25, 19, 29, 18, 11, 13, 17]
    target = 200
    print(subset_sum(iterable, target))


    #itunes Entry
    itunes_list = iTunesEntryReader("itunes_file.txt")

    print(subset_sum(itunes_list, 3600))
    print(subset_sum(itunes_list, 600))
    print(subset_sum(itunes_list, 60))
    print(subset_sum(itunes_list, 3600))
