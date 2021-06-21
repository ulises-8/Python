"""
CS3B, Assignment #8, Local Dictionary
Ulises Marian
Testing
"""

import unittest
import json

from assignment08 import *

# class DictionaryEntryTestCase(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     # def testInit(self):
#     #     dict_entry = DictionaryEntry("hola", "verb", "nice")
#     #     expected = ("Word : hola \
#     #                 Part of speech : verb \
#     #                 Definition : nice \
#     #                 Example : None")
#     #     actual = dict_entry("hola", "verb", "nice")
#     #     self.assertMultiLineEqual(expected, actual)
#
# class LocalDictionaryTestCase(unittest.TestCase):
#     def setUp(self):
#         self.local_dictionary = LocalDictionary()
#
#
#     def testDeserializedEntries(self):
#         expected: "{'copyright': 'foothill cs3b', 'purpose': 'sample " \
#                   "dictionary.json for assignment #8', 'todo':\
#                     'add at least 3 more words with part of speech, " \
#                   "definition, and optionally example of usage',\
#                     'entries':,\
#                     [<__main__.DictionaryEntry object at 0x7fd75099b550>,\
#                     <__main__.DictionaryEntry object at 0x7fd75099b790>,\
#                     <__main__.DictionaryEntry object at 0x7fd75099b820>,\
#                     <__main__.DictionaryEntry object at 0x7fd75099b8b0>,\
#                     <__main__.DictionaryEntry object at 0x7fd75099b940>,\
#                     <__main__.DictionaryEntry object at 0x7fd75099bac0>,\
#                     <__main__.DictionaryEntry object at 0x7fd75099bc40>]\
#                     , 'example': None}"
#         actual: self.local_dictionary.deserialize_entries()
#         #self.assertEqual(expected, actual)
#
#
#     # def testDeserializedEntries2(self):
#     #     expected: "{'copyright': 'foothill cs3b', 'purpose': 'sample " \
#     #               "dictionary.json for assignment #8', 'todo':\
#     #                 'add at least 3 more words with part of speech, " \
#     #               "definition, and optionally example of usage',\
#     #                 'entries':,\
#     #                 [<__main__.DictionaryEntry object at 0x7fd75099b550>,\
#     #                 <__main__.DictionaryEntry object at 0x7fd75099b790>,\
#     #                 <__main__.DictionaryEntry object at 0x7fd75099b820>,\
#     #                 <__main__.DictionaryEntry object at 0x7fd75099b8b0>,\
#     #                 <__main__.DictionaryEntry object at 0x7fd75099b940>,\
#     #                 <__main__.DictionaryEntry object at 0x7fd75099bac0>,\
#     #                 <__main__.DictionaryEntry object at 0x7fd75099bc40>]\
#     #                 , 'example': None}"
#     #     actual: with open("dictionary.json") as file:
#     #                 self.my_entries = json.load(file, object_hook=my_decode)
#
#
#     # def testAppendEntries(self):
#     #     expected = "Word : ace, Part of speech : noun
#     #                 Definition : a playing card with a single spot on it, ranked as the highest card in its suit in most card games
#     #                 Example : life had started dealing him aces again
#     #
#     #                 Word : python
#     #                 Part of speech : noun
#     #                 Definition : a large heavy-bodied non-venomous snake occurring throughout the Old World tropics, killing prey by constriction and asphyxiation.
#     #                 Example : None
#     #
#     #                 Word : foothill
#     #                 Part of speech : noun
#     #                 Definition : a low hill at the base of a mountain or mountain range
#     #                 Example : the camp lies in the foothills of the Andes
#     #
#     #                 Word : fly
#     #                 Part of speech : verb
#     #                 Definition : (of a bird, bat, or insect) move through the air using wings
#     #                 Example : he was sent flying by the tackle
#     #
#     #                 Word : avocado
#     #                 Part of speech : noun
#     #                 Definition : a pear-shaped fruit with a rough leathery skin
#     #                 Example : Avocado is a great source of nutrients
#     #
#     #                 Word : garlic
#     #                 Part of speech : noun
#     #                 Definition : a strong smelling vegetable, used as a flavouring in cooking
#     #                 Example : Garlic possesses potent antioxidant properties
#     #
#     #                 Word : onion
#     #                 Part of speech : noun
#     #                 Definition : an edible bulb with a pungent taste used in cooking
#     #                 Example : Onions are delicious"
#     #
#     #     actual = LocalDictionary.append_entries(self):
#     #     self.assertEqual(expected, actual)
#
#     def testSearch(self):
#         expected =( "Word : garlic "
#                     "Part of speech : noun"
#                     "Definition : a strong smelling vegetable, used as a flavouring in cooking"
#                     "Example : Garlic possesses potent antioxidant properties")
#         actual = self.local_dictionary.search("garlic")
#         self.assertEqual(expected, actual)
#
#     def testSearch2(self):
#         #without "example" parameter"
#         expected: ("Word : python"
#                    "Part of speech : noun"
#                    "Definition : a large heavy-bodied non-venomous snake "
#                    "occurring throughout the Old World tropics, "
#                    "killing prey by constriction and asphyxiation."
#                    "Example : None")
#         actual = self.local_dictionary.search("python")
#         #self.assertEqual(expected, actual)
#
#         #test KeyError
#         with self.assertRaises(KeyError):
#             self.local_dictionary.search("not in dictionary")


class DictionaryEntryCacheTestCase(unittest.TestCase):
    def setUp(self):
        self.entry_cache = DictionaryEntryCache(2)
        new_entries_list = []
        self.local_dict = LocalDictionary()
        for entry in self.local_dict.py_dictionary:
            new_entries_list.append(self.local_dict.py_dictionary[entry])

        self.entry_1 = new_entries_list[0] # "ace"
        self.entry_2 = new_entries_list[1]
        self.entry_3 = new_entries_list[2]
        self.entry_4 = new_entries_list[3]
        self.entry_5 = new_entries_list[4] #avocado
        self.entry_6 = new_entries_list[5]
        self.entry_7 = new_entries_list[6]
        self.entry_cache.add(self.entry_2)

    def testAdd(self):
        #add "avocado"
        expected = self.entry_4
        actual = self.entry_cache.add(self.entry_4) #avocado
        self.assertEqual(expected, actual)

        #add "ace"
        expected = self.entry_1
        actual = self.entry_cache.add(self.entry_1) # "ace"
        self.assertEqual(expected, actual)

        # add "foothill"
        expected = self.entry_3
        actual = self.entry_cache.add(self.entry_3)  # "foothill"
        self.assertEqual(expected, actual)


    def testSearch(self):
        #"avocado"
        expected = "Word : avocado" \
                   "Part of speech : noun" \
                   "Definition : a pear-shaped fruit with a rough leathery skin" \
                   "Example : Avocado is a great source of nutrients"
        actual = self.entry_cache.search("avocado")
        self.assertEqual(expected, actual)

        #"ace"
        expected = "Word : ace" \
                   "Part of speech : noun" \
                   "Definition : a playing card with a single spot on it," \
                   " ranked as the highest card in its suit in most card games" \
                   "Example : life had started dealing him aces again"
        actual = self.entry_cache.search("ace")
        self.assertEqual(expected, actual)

        #"aim"
        expected = "Word : foothill" \
                   "Part of speech : noun" \
                   "Definition : a low hill at the base of " \
                   "a mountain or mountain range" \
                   "Example : the camp lies in the foothills of the Andes"
        actual = self.entry_cache.search("foothill")
        self.assertEqual(expected, actual)


class Dictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary()
        self.local_dictionary = LocalDictionary()
        self.entry_cache = DictionaryEntryCache()

    def testSearch(self):
        expected = "Word : avocado" \
                   "Part of speech : noun" \
                   "Definition : a pear-shaped fruit with a rough leathery skin" \
                   "Example : Avocado is a great source of nutrients"
        actual = self.dictionary.local_dictionary.search("avocado")
        self.assertEqual(expected, actual)


        expected = "Word : onion" \
                   "Part of speech : noun" \
                   "Definition : an edible bulb with a " \
                   "pungent taste used in cooking" \
                   "Example : Onions are delicious"
        actual =  self.dictionary.local_dictionary.search("onion")
        self.assertEqual(expected, actual)

        expected = "(<__main__.DictionaryEntry object at 0x7ffe6b995c40>, 'Found in LOCAL\n')"
        actual = self.dictionary.search("onion")

        # "avocado" comes from LOCAL
        expected = "Word : avocado" \
                   "Part of speech : noun" \
                   "Definition : a pear-shaped fruit with a rough leathery skin" \
                   "Example : Avocado is a great source of nutrients" \
                   "Found in LOCAL"
        actual =actual = (self.dictionary.search("avocado")[0],
                  self.dictionary.search("avocado")[1])
        self.assertEqual(expected, actual)

        # "avocado" comes from CACHE
        expected = "Word : avocado" \
                   "Part of speech : noun" \
                   "Definition : a pear-shaped fruit with a rough leathery skin" \
                   "Example : Avocado is a great source of nutrients" \
                   "Found in CACHE"
        actual = actual = (self.dictionary.search("avocado")[0],
                           self.dictionary.search("avocado")[1])
        self.assertEqual(expected, actual)

        # "onion" comes from LOCAL
        expected = "Word : onion" \
                   "Part of speech : noun" \
                   "Definition : an edible bulb with" \
                   " a pungent taste used in cooking" \
                   "Example : Onions are delicious" \
                   "Found in LOCAL"
        actual = (self.dictionary.search("onion")[0],
                  self.dictionary.search("onion")[1])
        self.assertEqual(expected, actual)

        # "onion" comes from CACHE
        expected = "Word : onion" \
                 "Part of speech : noun" \
                 "Definition : an edible bulb with" \
                 " a pungent taste used in cooking" \
                 "Example : Onions are delicious" \
                 "Found in CACHE"
        actual = (self.dictionary.search("onion")[0],
                  self.dictionary.search("onion")[1])
        self.assertEqual(expected, actual)

        # "garlic" comes from LOCAL
        expected = "Word : garlic" \
                   "Part of speech : noun" \
                   "Definition : a strong smelling vegetable, " \
                   "used as a flavouring in cooking" \
                   "Example : Garlic possesses potent antioxidant properties" \
                   "Found in LOCAL"
        actual = (self.dictionary.search("garlic")[0],
                  self.dictionary.search("onion")[1])
        self.assertEqual(expected, actual)

        # "garlic" comes from CACHE
        expected = "Word : garlic" \
                   "Part of speech : noun" \
                   "Definition : a strong smelling vegetable, " \
                   "used as a flavouring in cooking" \
                   "Example : Garlic possesses potent antioxidant properties" \
                   "Found in CACHE"
        actual = (self.dictionary.search("garlic")[0],
                  self.dictionary.search("onion")[1])
        self.assertEqual(expected, actual)

        # test KeyError
        with self.assertRaises(KeyError):
            self.dictionary.local_dictionary.search("nothing")

        with self.assertRaises(KeyError):
            self.dictionary.search("mistake")

        with self.assertRaises(KeyError):
            self.dictionary.search("again")

        with self.assertRaises(KeyError):
            self.dictionary.search("NotFound")




if __name__ == "__main__":
 unittest.main()