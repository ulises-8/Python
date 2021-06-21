"""
CS3C, Assignment #7
Implementing HashMap
Ulises Marian
"""

from hashqp import *
#from ebook import *

class HashMap():
    def __init__(self):
        self.hash = HashQP()
        self.map = [[] for i in range(self.hash._nbuckets)]

    #not used
    def __str__(self):
        #return str(self.map)
        s = ""
        for element in self.map:
            s+= str(element)
        return s

        # s = ""
        # for element in self.map:
        #     if not element:
        #         continue
        #     for pair in element:
        #         s += str(pair)
        # return s

    def __getitem__(self, key):
        bucket_index = self.hash._hash(key)
        bucket = self.hash._buckets[bucket_index]
        for element in self.map[bucket_index]:
            if key == element[0]:
                return element[1]

    def __setitem__(self, key, value):
        bucket_index = self.hash._hash(key)
        bucket = self.hash._buckets[bucket_index]
        for element in self.map[bucket_index]:
            if key == element[0]:
                element[1] = value
                break
        else:
            bucket.item = key

        self.map[bucket_index].append([bucket.item, value])
        self.hash._nitems += 1

    def __iter__(self):
        for element in self.map:
            if not element:
                continue
            for key in element:
                yield key[0]

    def __eq__(self, other):
        self_pairs = self.__iter__()
        for key in self_pairs:
            if self[key] != other[key]:
                return False
        other_pairs = other.__iter__()
        for key in other_pairs:
            if other[key] != self[key]:
                return False
        return True

def main():
    hashmap = HashMap()
    print(hasattr(hashmap, "hash"))

main()
