# anagram.py -- find the case-insensitive anagrams of input words.
# Copyright (c) 2015 Scott Cheloha.  All rights reserved.
# See LICENSE for complete licensing details.

from itertools import permutations
import argparse

wordSet = set()

# Strip whitespace from a string and lowercase it
def strip_and_lower(s):
    return s.lower().strip()

# Return true if the lowercased/stripped inputWord appears
# in the global wordSet
def dictionaryLookup(inputWord):
    return(strip_and_lower(inputWord) in wordSet)

# Given an input word, returns all permutations of the word found
# in the input dictionary
def findAnagrams(inputWord):
    # Get a list of permutations of the characters in the input word
    perms = set(''.join(p) for p in permutations(inputWord))
    perms.remove(inputWord)

    # anagrams is just the sublist of perms that returns true
    # on a call to dictionaryLookup()
    anagrams = list(p for p in perms if dictionaryLookup(p))
    return anagrams

def main(words, dictFilename):
    # Read the words from our dictionary file into wordSet
    dictFile = open(dictFilename, 'r')
    global wordSet
    wordSet = set(strip_and_lower(w) for w in dictFile.read().splitlines())
    dictFile.close()

    # Find the anagrams for every string given as input to the script
    for w in words:
        print(w + ": ", end="")

        anagrams = findAnagrams(w)
        for a in anagrams:
            print(a, end=", ")

        # Get rid of the dangling ", " if necessary
        if len(anagrams) > 0:
            print("\b\b ", end="")
        print("")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Prints the case-insensitive anagrams of words.')
    parser.add_argument('words', metavar='W', type=str, nargs='+',
                   help='word you want the anagrams for')
    parser.add_argument('-d', dest='dictionary', type=str,
                        default="/usr/share/dict/words",
            help='path to dictionary file (default: /usr/share/dict/words)')

    args = parser.parse_args()
    main(args.words, args.dictionary)
