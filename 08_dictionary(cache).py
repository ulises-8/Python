"""
CS3B, Assignment #8, Local Dictionary
Ulises Marian
"""

import json
from datalist import *
from enum import Enum

class DictionaryEntry:
    def __init__(self, word, part_of_speech, definition, example=None):
        self.word = word
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example

    def __str__(self):
        return f"Word : {self.word:}\n" \
               f"Part of speech : {self.part_of_speech}\n" \
               f"Definition : {self.definition}\n" \
               f"Example : {self.example}\n"

    def get_word(self):
        return self.word

class LocalDictionary:
    def __init__(self, dictionary_json_name="dictionary.json"):
        self.dictionary = dictionary_json_name
        self.py_dictionary = dict({})
        self.deserialize_entries()
        self.append_entries()

    # deserialize each entry into an instance of DictionaryEntry
    def deserialize_entries(self):
        with open("dictionary.json") as file:
            self.my_entries = json.load(file, object_hook=my_decode)
            #print(self.my_entries)

    def append_entries(self):
        #append entries to new dict (py.dict)
        for entry in self.my_entries["entries"]: #index list "entries" in json
            self.py_dictionary[entry.word] = entry

    def search(self, word):
        if word in self.py_dictionary:
            return self.py_dictionary[word]
        else:
            raise KeyError(f"Error: entry for '{word}' not found")

def my_decode(o):
    try:
        if "example" in o:
            return DictionaryEntry(o["word"],
                                   o["part_of_speech"],
                                   o["definition"],
                                   o["example"])
        else:
            o["example"] = None  #set key "example"
            return DictionaryEntry(o["word"],
                                   o["part_of_speech"],
                                   o["definition"])
    except:
        return o

class DataList(LinkedList):
    """
    DataList can store arbitrary data
    """
    def get_head(self):
        return super().get_head()

    def add_to_head(self, data):
        super().add_to_head(DataNode(data))

    def remove_from_head(self):
        return super().remove_from_head().data

    def insert_sorted(self, data):
        temp = self.head
        while temp.next:
            if data <= temp.next.data:
                break
            temp = temp.next
        temp.insert_after(DataNode(data))

    def remove_end(self):
        if self.head is None:  #when list is empty
            return
        temp = self.head
        while temp.next.next: #temp has to be one node before the last node
            temp = temp.next   # thus temp.next.next and not temp.next
        Node.remove_after(temp)


class DictionaryEntryCache(DataList):
    def __init__(self, capacity=10):
        super().__init__()
        if capacity < 1:
            raise ValueError
        self.capacity = capacity
        self.count = 0

    def add(self, entry):
        if type(entry) != DictionaryEntry:
            raise TypeError
        if self.count < self.capacity:
            self.add_to_head(entry)
            self.count += 1
        else:
            self.remove_end()
            self.add_to_head(entry)

    def search(self, word):
        temp = self.get_head().next
        while temp:
            if temp.data.get_word() == word:
                self.add(temp.data)
                return temp.data
            else:
                temp = temp.next
        raise KeyError

class DictionarySource(Enum):  #it's an enum
    LOCAL = 1
    CACHE = 2

class Dictionary:
    def __init__(self):
        self.local_dictionary = LocalDictionary()
        self.entry_cache = DictionaryEntryCache()

    def search(self, word):
        try:
            return (self.entry_cache.search(word),
                    f"Found in {DictionarySource.CACHE.name}\n")
        except KeyError:
            try:
                entry_found = self.local_dictionary.search(word)
                self.entry_cache.add(entry_found)
                return entry_found, f"Found in {DictionarySource.LOCAL.name}\n"
            except KeyError:
                raise

def main():
    dictionary = Dictionary()
    while True:
        user_search = input("Enter a word to search: ")
        try:
            result = dictionary.search(user_search)
            print(result[0], result[1])
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
    #test()

# def test():
#
#     #deserialize json file
#     #deserialize each entry into an instance of DictionaryEntry,thus use object_hook
#     with open("dictionary.json") as file:
#         my_entries = json.load(file, object_hook=my_decode)
#
#
#     local_dict = LocalDictionary()
#     #print(local_dict.py_dictionary)   #here, dictionary is empty
#
#     # append entries to new dict (py.dict)
#     #index the word "entries" in my_entries,
#     # because "entries" has a list of the entries we want
#     #not interested in the things before "entries", e.g., "copyright", etc.
#     for entry in my_entries["entries"]:
#         local_dict.py_dictionary[entry.word] = entry
#         #print(entry.word)
#         #dict_entry = DictionaryEntry()
#     #print("LOCAL DICTIONARY.py_dictionary", local_dict.py_dictionary)  #now
#     # py_dictionary has
#     # the entries
#
#     #print(type(local_dict.py_dictionary))
#     #very important piece of code
#     # try:
#     #     print(local_dict.search("python"))
#     # except KeyError:      #handling TypeError raised in def search()
#     #     print("no match found")
#
#
#     entry_cache = DictionaryEntryCache(capacity=5)
#
#
#     new_entries_list = []
#     for entry in local_dict.py_dictionary:
#         new_entries_list.append(local_dict.py_dictionary[entry])
#
#     entry_1 = new_entries_list[0]
#     entry_2 = new_entries_list[1]
#     entry_3 = new_entries_list[2]
#     entry_4 = new_entries_list[3]
#     entry_5 = new_entries_list[4]
#     entry_6 = new_entries_list[5]
#     entry_7 = new_entries_list[6]
#
#
#     lisst_w_entries = [entry_1, entry_2, entry_3, entry_4, entry_5, entry_6,
#                        entry_7]
#     print("lisst_w_entries", lisst_w_entries)
#
#     #print(entry_3)
#     #print("THIS", local_dict.py_dictionary)
#
#     #for i in local_dict.py_dictionary:
#     #print(entry_cache.add(entry_1))
#     #print(entry_cache.search(("garlic")))
#     #print(entry_cache)
#
#     for i in lisst_w_entries:
#         entry_cache.add(i)
#
#     #print(entry_cache.search(("foothill")))
#     # print("entry_cache:", entry_cache)
#     #
#     #
#     # try:
#     #     print(entry_cache.search("onion"))
#     # except KeyError:
#     #     print("word not found")
#
#
#
#
#
#
#
