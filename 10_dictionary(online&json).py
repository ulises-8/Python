"""
CS3B, Assignment #10, Online Dictionary
Ulises Marian
"""

import time
import requests
import json
from enum import Enum
from http import HTTPStatus

from datalist import *

class DictionaryEntry:
    def __init__(self, word, part_of_speech, definition, example=None):
        self.word = word
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example

    def __str__(self):
        return f"Word          : {self.word}\n" \
               f"Part of speech: {self.part_of_speech}\n" \
               f"Definition    : {self.definition}\n" \
               f"Example       : {self.example}"


class LocalDictionary:
    def __init__(self, dictionary_json_name="dictionary.json"):
        with open(dictionary_json_name) as file:
            self._dictionary = {}
            data = json.load(file, object_hook=self.dictionary_entry_decoder)
            for d in data["entries"]:
                if isinstance(d, DictionaryEntry):
                    # If entry doesn't have all the required fields, it's not
                    # converted to DictionaryEntry, so we don't add it to dict.
                    # Use .lower() to make search case-insensitive, though that's
                    # not required.  Requires the same in search().
                    self._dictionary[d.word.lower()] = d

    def dictionary_entry_decoder(self, o):
        try:
            # This line works, but we haven't talked about ** by this point.
            # return DictionaryEntry(**o), so the longer version.
            if "example" in o:
                example = o["example"]
            else:
                example = None

            # We can also put this directly in self.dictionary, but this stays
            # closer to what the examples in the lectures did.
            return DictionaryEntry(word=o["word"],
                                   part_of_speech=o["part_of_speech"],
                                   definition=o["definition"],
                                   example=example)
        except:
            # If there's an error deserialize o, just return it as is, otherwise
            # it won't get deserialized at all.
            return o

    def search(self, word):
        # Use .lower() to make search case-insensitive, though that's
        # not required by the assignment.
        return self._dictionary[word.lower()]


class DictionaryEntryCache(DataList):
    MIN_CAPACITY = 1

    def __init__(self, capacity=1):
        super().__init__()
        if capacity < self.MIN_CAPACITY:
            raise ValueError("Capacity should be at least 1")
        self.capacity = capacity
        self.count = 0

    def add(self, entry):
        if not isinstance(entry, DictionaryEntry):
            raise TypeError("entry should be DictionaryEntry")
        self.add_to_head(entry)
        self.count += 1
        if self.count > self.capacity:
            self.remove_tail()

    def remove_tail(self):
        self.reset_current()
        current = self.iterate()
        # While we typically shouldn't mix iteration with modification to the list being
        # iterated, we stop iteration as soon as we remove the last node, so that's ok.
        while current:
            if current.next is None:
                # If this is true, there's only 1 data node, which should never happen
                # because we ensure capacity is at least 1, and we call remove_tail()
                # only after adding another entry, so there are always at least 2.
                raise RuntimeError("Something's very wrong")

            if current.next.next is None:
                # current.next is the last (oldest) one, remove it
                current.remove_after()
                break
            current = self.iterate()
        self.count -= 1

    def search(self, word):
        self.reset_current()
        current = self.iterate()
        while current:
            # Case-insensitive comparison, though not required.
            if current.data.word.lower() == word.lower():
                # Found the entry with the right word, remove it from the list,
                # and insert it at the head.  Return it.
                entry = current.data
                self.remove(entry)
                self.add_to_head(entry)
                return entry
            current = self.iterate()
        raise KeyError(f"Cannot find {word}")


class OxfordDictionary(LocalDictionary):

    #class constants
    APP_ID =  "c2f6e385"
    APP_KEY = "1708179f5153cc68d2f7430876c5003a"

    def search(self, word):
        self.word = word

        language = "en-us"
        word_id = self.word

        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/"\
              + language + "/" + word_id.lower()

        r = requests.get(url, headers={"app_id": OxfordDictionary.APP_ID,
                                       "app_key": OxfordDictionary.APP_KEY})

        if r.status_code == HTTPStatus.OK:
            json_resp = r.json()
        else:
            raise KeyError(f"word '{word}' not found")

        # create DictionaryEntry instance with the following:
        lexical_id = (json_resp["results"][0]["lexicalEntries"][0]
                      ["lexicalCategory"]["id"])
        definition = (json_resp["results"][0]["lexicalEntries"][0]
                      ["entries"][0]["senses"][0]["definitions"][0])

        try:
            example = (json_resp["results"][0]["lexicalEntries"][0]
                      ["entries"][0]["senses"][0]["examples"][0]["text"])
        except:
            example=None


        return(DictionaryEntry(word_id, lexical_id, definition, example))


class DictionarySource(Enum):
    LOCAL = 1
    CACHE = 2
    OXFORD_ONLINE = 3

    def __str__(self):
        return self.name


class Dictionary:
    def __init__(self, source=DictionarySource.OXFORD_ONLINE):
        if source is DictionarySource.OXFORD_ONLINE:
            self.dictionary = OxfordDictionary()
        elif source is DictionarySource.LOCAL:
            self.dictionary = LocalDictionary()
        else:
            raise ValueError

        self.dictionary_source = source
        self.dictionary_entry_cache = DictionaryEntryCache(1)

    def search(self, word):
        try:
            result_tuple = time_func(self.dictionary_entry_cache.search, word)
            return (result_tuple[0], DictionarySource.CACHE, result_tuple[1])
        except KeyError:
            result_tuple = time_func(self.dictionary.search, word)
            self.dictionary_entry_cache.add(result_tuple[0])
            return (result_tuple[0], self.dictionary_source, result_tuple[1])


def time_func(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    duration = time.perf_counter() - start
    return result, duration


def main():
    dictionary = Dictionary()
    while True:
        word = input("Enter a word to lookup: ")
        try:
            entry, source, duration = dictionary.search(word)
            print(f"{entry}\n(Found in {source} in {duration} seconds)\n")
        except KeyError as e:
            print(f"Error when searching: {str(e)}\n")
        except requests.ConnectionError:
           print(f"NO internet connection\n")



if __name__ == '__main__':
    main()
