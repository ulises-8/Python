"""
CS3B, Assignment #10, Online Dictionary
Ulises Marian
Testing
"""

import unittest
import json
from assignment10 import *

class TimeFuncTest(unittest.TestCase):
    def testTimeFunc(self):
        #1 test
        expected = (340282366920938463463374607431768211456,
                  2.303000000009048e-06)
        actual = result, duration = time_func(pow, 2, 128)
        self.assertEqual(expected[0], actual[0])    #result

        # self.assertAlmostEqual(expected[1], actual[1])    #duration

        #2 test
        expected2 = (None, 4.4303999999995014e-05)
        actual2 = result, duration = time_func(print, "hello", "world",
                                               sep="\n")
        self.assertEqual(expected2[0], actual2[0])    #result

        # self.assertAlmostEqual(expected2[1], actual2[1])   #duration

        #3 test
        expected = (777, 9.570000000236334e-07)
        actual = result, duration = time_func(abs, 777)
        self.assertEqual(expected[0], actual[0])

class OxfordDictionaryTest(unittest.TestCase):
    dictionary = OxfordDictionary()
    def testSearch(self):
        #1 word, no example
        word = "cheetah"
        entry = self.dictionary.search(word)
        self.assertEqual(word, entry.word)
        # no example, cheetah
        example = None
        entry_example = entry.example
        self.assertEqual(example, entry.example)

        #2 word w/example
        word = "red"
        entry = self.dictionary.search(word)
        self.assertEqual(word, entry.word)

        part_of_speech = "adjective"
        part_of_speech_entry = entry.part_of_speech
        self.assertEqual(part_of_speech, part_of_speech_entry)

        example = "her red lips"
        entry_example = entry.example
        self.assertEqual(example, entry.example)

        #3 word w/example
        word = "light"
        entry = self.dictionary.search(word)
        self.assertEqual(word, entry.word)

        part_of_speech = "noun"
        part_of_speech_entry = entry.part_of_speech
        self.assertEqual(part_of_speech, part_of_speech_entry)

        definition = "the natural agent that stimulates sight " \
                     "and makes things visible"
        definition_entry = entry.definition
        self.assertEqual(definition, definition_entry)

        example = "the light of the sun"
        entry_example = entry.example
        self.assertEqual(example, entry.example)

        #4 word, no example
        word = "tiger"
        entry = self.dictionary.search(word)
        self.assertEqual(word, entry.word)

        part_of_speech = "noun"
        part_of_speech_entry = entry.part_of_speech
        self.assertEqual(part_of_speech, part_of_speech_entry)

        definition = "a very large solitary cat with a yellow-brown coat" \
                     " striped with black, native to the forests of Asia" \
                     " but becoming increasingly rare."
        definition_entry = entry.definition
        self.assertEqual(definition, definition_entry)

        example = None
        entry_example = entry.example
        self.assertEqual(example, entry.example)

    def testSearchFailure(self):
        with self.assertRaises(KeyError):
            self.dictionary.search("correkt")

        with self.assertRaises(KeyError):
            self.dictionary.search("neber wrung")

        with self.assertRaises(KeyError):
            self.dictionary.search("dneiqond")


class DiciontaryTest(unittest.TestCase):
    def testSourceAndDuration(self):
        #1 example
        dictionary = Dictionary()
        #source should be OXFORD_ONLINE
        word = "movie"
        expected_source = "OXFORD_ONLINE"
        actual_source = dictionary.search(word)
        actual_duration = actual_source[2]
        self.assertEqual(expected_source, actual_source[1].name)
        #duration
        #source should be Cache
        word = "movie"
        expected_source2 = "CACHE"
        actual_source2 = dictionary.search(word)
        actual_duration2 = actual_source2[2]
        #found in CACHE
        self.assertEqual(expected_source2, actual_source2[1].name)
        #cache much faster
        self.assertLess(actual_duration2, actual_duration)

        #2 example
        dictionary = Dictionary()
        # source should be OXFORD_ONLINE
        word = "soccer"
        expected_source = "OXFORD_ONLINE"
        actual_source = dictionary.search(word)
        actual_duration = actual_source[2]
        self.assertEqual(expected_source, actual_source[1].name)
        # duration
        # source should be Cache
        word = "soccer"
        expected_source2 = "CACHE"
        actual_source2 = dictionary.search(word)
        actual_duration2 = actual_source2[2]
        # found in CACHE
        self.assertEqual(expected_source2, actual_source2[1].name)
        # cache much faster
        self.assertLess(actual_duration2, actual_duration)

        #3 example
        dictionary = Dictionary()
        # source should be OXFORD_ONLINE
        word = "fast"
        expected_source = "OXFORD_ONLINE"
        actual_source = dictionary.search(word)
        actual_duration = actual_source[2]
        self.assertEqual(expected_source, actual_source[1].name)
        # duration
        # source should be Cache
        word = "fast"
        expected_source2 = "CACHE"
        actual_source2 = dictionary.search(word)
        actual_duration2 = actual_source2[2]
        # found in CACHE
        self.assertEqual(expected_source2, actual_source2[1].name)
        # cache much faster
        self.assertLess(actual_duration2, actual_duration)



if __name__ == "__main__":
 unittest.main()