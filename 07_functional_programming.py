"""
CS3B, Assignment #7, map, filter, reduce
Ulises Marian
"""


class MfrList(list):
    """A class that's a Python list with map(), filter(), reduce() added"""

    @staticmethod
    def validate_func(func):
        """Validate func is callable, raises TypeError if not"""
        if not callable(func):
            raise TypeError(f"'{type(func)}' is not callable")

    def map(self, func):
        """Applies func to each element, returns a new MfrList"""
        self.validate_func(func)
        return MfrList([func(e) for e in self])

    def filter(self, func):
        self.validate_func(func)
        list_ = MfrList()
        for e in self:    # for element in self(the list)
            if bool(func(e)) is True: #apply func on each e, and bool() it
                list_.append(e)   # check if it is True, if it is, append it
        return list_

    def reduce(self, func, initial=None):
        self.validate_func(func)
        # if list/iterable is empty and initial is None
        if len(self) == 0 and initial is None:
            raise TypeError
        elif len(self) == 1 and initial is None:
            return self[0]           #for e in self:
                                          #return e
        #if list/iterable is empty and initial is not None
        elif len(self) == 0 and initial is not None:
            return initial
        # if initial is not none, apply func to it and to the list's 1st element
        elif initial is not None:
            result = func(initial, self[0])
            for e in self[1:]:           #iterate starting on the second element
                result = func(result, e)
            return result
        # if list not empty and initial is None
        elif len(self) != 0 and initial is None:
            result = func(self[0], self[1])  #apply func to the first 2 elements
            for e in self[2:]:            #iterate starting on the third element
                result = func(result, e)
            return result

    def __iter__(self):
        self._n = 0
        return self   # return self, because given that MfrList inherits from
                        # list, it is itself an iterable

    def __next__(self):
        if self._n >= len(self): #if self._n is greater than the length of the
                      # iterable, i.e., > than the # of elements it can iterate
                      # over, raise...
            raise StopIteration

        n = self._n
        self._n += 1
        return self[n]  # return the value of the element at the given index
                            # currently being iterated over

# map() example
def square(mfrlist):
    """Square every element in the list"""
    return mfrlist.map(lambda x: x ** 2)

# filter() example
def odds(mfrlist):
    """Return a new list with all the odd numbers in the list"""
    return mfrlist.filter(lambda x: x % 2 == 1)

# reduce() example
def add_all(mfrlist):
    """Sum up all elements in the list"""
    return mfrlist.reduce(lambda a, b: a + b, 0)

# map()/reduce() example
def sum_of_squares(mfrlist):
    """Add up the squares of all elements in the list"""
    return (mfrlist
            .map(lambda x: x ** 2)
            .reduce(lambda a, b: a + b, 0))

def is_in(mfrlist, key):
    """Return True if key is in mfrlist, False otherwise"""
    return (mfrlist
            .map(lambda e: e == key)
            .reduce(lambda a, b: a or b, False))

#My functions

def capitalize(mfrlist):
    return mfrlist.map(lambda x : x.capitalize())

def between(mfrlist, inclusive_start, exclusive_end):
    return (mfrlist.filter(lambda x: x >= inclusive_start and x
                            <= exclusive_end))

def oldest(mfrlist):
    return (mfrlist.reduce(lambda a, b: a if a[1] > b[1] else b))[0]
    #the whole expression above inside () is a tuple because it is
    # returning either a or b, which are tuples, and then I just extract the
    # element at index --> [0]

def join(mfrlist, sep):
    try:
        return(mfrlist.reduce(lambda a, b: str(str(a) + str(sep) + str(b))))
    except:
        return ""

def same(mfrlist):   #each element in mfrlist is being compared to mfrlist[0]
     new_list = mfrlist.filter(lambda x: True if x == mfrlist[0] else
     False)

     return (mfrlist.reduce(lambda a, b: True if new_list == mfrlist else
     False, True))

def count_str(mfrlist, key):
    counter = 0
    return(mfrlist.map(lambda a: counter+1 if a.lower() == key.lower() else
    False).reduce(lambda a, b: a + b, counter))

def longest_palindrome(mfrlist):
    return (mfrlist.filter(lambda x:x==x[::-1])
            .reduce(lambda a, b : a if a > b else b))

def test():
    """Sample usage"""
    tuplist = MfrList([("Zlatan", 19), ("Lukaku", 27), ("Bamboo", 90)])
    lisst = MfrList(["hoy", "mañana", "Hoy", "mañAnA", "HOY"])
    palist = MfrList(["cake", "noon", "nun", "racecar"])
    mfrlist = MfrList([12, 98, 53, 12])
    empty = MfrList([])

    print("filter ", mfrlist.filter(lambda x: x % 2 == 1))
    print(f"square({mfrlist}) => {square(mfrlist)}")
    print(f"REDUCE: add_all({mfrlist}) => {add_all(mfrlist)}")
    print(f"odds({mfrlist}) => {odds(mfrlist)}")

    print(f"capitalize: {capitalize(lisst)}")
    print(f"between: {between(mfrlist, 10, 60)}")
    print(f"oldest: {oldest(tuplist)}")
    print("join: ", join(MfrList([]), "-")) # if list empty, print ""
    print(f"same: {same(MfrList([4, 4, 4]))}")
    print("count_str: ", count_str(empty, "hoy"))
    print("longest palindrome: ", longest_palindrome(palist))
    #Python built-in map
    print("line 174 built in map ", list(map(lambda x: x ** 2, mfrlist)))
    print("line175 my reduce", mfrlist.reduce(lambda x, y: x + y))
    print(mfrlist.filter(lambda x: x == 12))
    print("line last ", capitalize(lisst))
    # iterator
    list_ = MfrList([8, 3, 9])
    # create an iterable
    iterable = list_.__iter__()
    print(f"iterable: {iterable}")
    print(iterable.__next__())
    print(iterable.__next__())
    print(iterable.__next__())
    print(iterable.__next__())    #raise StopIteration expected


if __name__ == '__main__':
    test()
