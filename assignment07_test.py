"""
CS3C, Assignment #7
Implementing HashMap
Ulises Marian
"""

from assignment07 import *
from ebook import *
import unittest

class HashMapTestCase(unittest.TestCase):
    def testInit(self):
        hashmap = HashMap()
        expected = "[][][][][][][][][][][][][][][][][][][][][][][][][][][]" \
                   "[][][][][][][][][][][][][][][][][][][][][][][][][][][]" \
                   "[][][][][][][][][][][][][][][][][][][][][][][][][][][]" \
                   "[][][][][][][][][][][][][][][][]"
        actual = hashmap.__str__()
        self.assertEqual(expected, actual)

    def testSetItem(self):
        hashmap = HashMap()
        hashmap["name"] = "Ulises"
        expected = [['name', 'Ulises']]
        self.assertIn(expected, hashmap.map)

    def testGetItem(self):
        hashmap = HashMap()
        hashmap["name"] = "Ulises"
        expected = "Ulises"
        actual = hashmap["name"]
        self.assertEqual(expected, actual)
        #changing value
        hashmap["name"] = "Batman"
        expected = "Batman"
        actual = hashmap["name"]
        self.assertEqual(expected, actual)
        self.assertNotEqual("Ulises", hashmap["name"])

    def testSetItem2(self):
        hashmap = HashMap()
        hashmap["color"] = "red"
        expected = [['color', 'red']]
        self.assertIn(expected, hashmap.map)

    def testGetItem2(self):
        hashmap = HashMap()
        hashmap["color"] = "red"
        expected = "red"
        actual = hashmap["color"]
        self.assertEqual(expected, actual)

    def testSetItemChangeValue(self):
        hashmap = HashMap()
        hashmap["color"] = "red"

        expected = "red"
        actual = hashmap["color"]
        self.assertEqual(expected, actual)

        #change "color" value
        hashmap["color"] = "blue"
        expected = "blue"
        actual = hashmap["color"]
        self.assertEqual(expected, actual)
        #checking that "red" is not longer the value associated with 'color' key
        self.assertNotEqual("red",hashmap["color"] )

        # change "color" value again
        hashmap["color"] = "yellow"
        expected = "yellow"
        actual = hashmap["color"]
        self.assertEqual(expected, actual)
        # checking that "red" is not longer the value associated with 'color' key
        self.assertNotEqual("blue", hashmap["color"])


    def testSetGet(self):
        hashmap = HashMap()
        hashmap["drink"] = "beer"
        hashmap["country"] = "Brazil"
        hashmap["city"] = "Sao Paolo"
        hashmap["continent"] = "South America"
        hashmap["food"] = "shrimps"

        expected = "Brazil"
        actual = hashmap["country"]
        self.assertEqual(expected, actual)

        expected = "beer"
        actual = hashmap["drink"]
        self.assertEqual(expected, actual)

        expected = "Sao Paolo"
        actual = hashmap["city"]
        self.assertEqual(expected, actual)

        expected = "South America"
        actual = hashmap["continent"]
        self.assertEqual(expected, actual)

        expected = "shrimps"
        actual = hashmap["food"]
        self.assertEqual(expected, actual)

        hashmap["country"] = "Italy"
        hashmap["city"] = "Napoli"
        hashmap["continent"] = "Europe"

        expected = "Italy"
        actual = hashmap["country"]
        self.assertEqual(expected, actual)
        self.assertNotEqual("Brazil", hashmap["country"])

        expected = "Napoli"
        actual = hashmap["city"]
        self.assertEqual(expected, actual)
        self.assertNotEqual("Sao Paolo", hashmap["country"])

        expected = "Europe"
        actual = hashmap["continent"]
        self.assertEqual(expected, actual)
        self.assertNotEqual("South America", hashmap["country"])

    def testIter(self):
        hashmap = HashMap()
        hashmap["drink"] = "beer"
        hashmap["country"] = "Brazil"
        hashmap["city"] = "Sao Paolo"
        hashmap["continent"] = "South America"
        hashmap["food"] = "shrimps"

        expected = ["drink", "country", "city", "continent", "food"]

        keys_returned = []
        for key in hashmap:
            keys_returned.append(key)

        actual = keys_returned

        for key in expected:
            self.assertIn(key, keys_returned)

        for key in actual:
            self.assertIn(key, expected)

    def testIter2(self):
        hashmap = HashMap()
        nums = ["zero", "one", "two", "three", "four", "five", "six", "seven"]
        for i, num in enumerate(nums):
            hashmap[num] = i

        expected = nums

        keys_returned = []
        for key in hashmap:
            keys_returned.append(key)

        actual = keys_returned

        for key in expected:
            self.assertIn(key, keys_returned)

        for key in actual:
            self.assertIn(key, expected)

    def testEqual(self):
        hashmap1 = HashMap()
        hashmap1["drink"] = "beer"
        hashmap1["country"] = "Brazil"
        hashmap1["city"] = "Sao Paolo"
        hashmap1["continent"] = "South America"
        hashmap1["food"] = "shrimps"

        hashmap2 = HashMap()
        hashmap2["continent"] = "South America"
        hashmap2["food"] = "shrimps"
        hashmap2["drink"] = "beer"
        hashmap2["city"] = "Sao Paolo"
        hashmap2["country"] = "Brazil"

        self.assertEqual(hashmap1, hashmap2)

    def testEqual2(self):
        hashmap1 = HashMap()
        hashmap1["material"] = "metal"
        hashmap1["power"] = "electricity"
        hashmap1["height"] = "185"
        hashmap1["facemask"] = "always"
        hashmap1["animal"] = "cheetah"
        hashmap1["brain"] = "dolphin"
        hashmap1["language"] = "Python"
        hashmap1["vacations"] = "maybe"
        hashmap1["music"] = "cello"

        hashmap2 = HashMap()
        hashmap2["music"] = "cello"
        hashmap2["material"] = "metal"
        hashmap2["vacations"] = "maybe"
        hashmap2["power"] = "electricity"
        hashmap2["language"] = "Python"
        hashmap2["height"] = "185"
        hashmap2["brain"] = "dolphin"
        hashmap2["facemask"] = "always"
        hashmap2["animal"] = "cheetah"

        self.assertEqual(hashmap1, hashmap2)

        #change one key-value, thus hashmaps no longer equal to one another
        hashmap2["language"] = "Java"
        self.assertNotEqual(hashmap1, hashmap2)

        #now equal again
        hashmap1["language"] = "Java"
        self.assertEqual(hashmap1, hashmap2)

    def testProjectGutenburgMapByID(self):
        my_books = eBookEntryReader("catalog-short4.txt")

        map_by_id = HashMap()
        for book in my_books:
            create_list = [book.title, book.author, book.subject, book.id]
            book = eBookEntry(create_list)
            map_by_id[book.id] = book
            #print(map_by_id[book.id])

        #test 1
        expected = "24742: Stephens, James, 1882-1950 ->" \
                   " Mary, Mary (Mothers and daughters -- Fiction)"
        actual = str(map_by_id[24742])
        self.assertEqual(expected, actual)

        #test 2
        expected = "5900: Garis, Howard Roger, 1873-1962 ->" \
                   " Umboo, the Elephant (No Subject)"
        actual = str(map_by_id[5900])
        self.assertEqual(expected, actual)

        #test 3
        expected = "29946: Freud, Sigmund, 1856-1939 ->" \
                   " Eine Kindheitserinnerung aus »Dichtung und Wahrheit« (BF)"
        actual = str(map_by_id[29946])
        self.assertEqual(expected, actual)

        #test 4
        expected = "7218: Huang, Shigong, 3rd cent. B.C. -> 三略 " \
                   "(Military art and science -- China -- Early works to 1800)"
        actual = str(map_by_id[7218])
        self.assertEqual(expected, actual)


    def testProGutenburgMapByAuthorTitle(self):
        my_books = eBookEntryReader("catalog-short4.txt")

        map_author_title = HashMap()
        for book in my_books:
            create_list = [book.title, book.author, book.subject, book.id]
            book = eBookEntry(create_list)
            map_author_title[(book.author, book.title)] = book
            #print(map_author_title[(book.author, book.title)])

        #test 1
        expected = "27979: Zùccoli, Luciano, 1868-1929 -> La freccia nel fianco (PQ)"
        actual = str(map_author_title[("Zùccoli, Luciano, 1868-1929",
                                       "La freccia nel fianco")])
        self.assertEqual(expected, actual)

        #test 2
        expected = "2637: Tolstoy, Leo, graf, 1828-1910 -> " \
                   "Youth (Social problems -- Fiction)"
        actual = str(map_author_title[("Tolstoy, Leo, graf, 1828-1910",
                                       "Youth")])
        self.assertEqual(expected, actual)

        #test 3
        expected = "29711: Galsworthy, John, 1867-1933 -> Another Sheaf (Essays)"
        actual = str(map_author_title[("Galsworthy, John, 1867-1933",
                                       "Another Sheaf")])
        self.assertEqual(expected, actual)

        #test 4
        expected = "17410: Roig i Raventós, Josep, 1883-1966 -> Ànimes atuïdes (No Subject)"
        actual = str(map_author_title[("Roig i Raventós, Josep, 1883-1966",
                                       "Ànimes atuïdes")])
        self.assertEqual(expected, actual)

