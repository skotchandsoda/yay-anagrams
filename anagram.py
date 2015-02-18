# anagram.py:
#   Find
# Copyright (c) 2015 Scott Cheloha.  All rights reserved.

from itertools import permutations
import argparse


wordSet = set()

def strip_and_lower(s):
    return s.lower().strip()

def dictionaryLookup(inputWord):
    # Lowercase and strip the input word of whitespace, just in case
    return(strip_and_lower(inputWord) in wordSet)

# Given a string s, returns all permutations of s.  For example:
#   stringPermutations("lot") = ['lot', 'lto', 'olt', 'otl', 'tlo', 'tol']
def stringPermutations(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    else:
        perms = list()
        for character in s:
            sub_perms = stringPermutations(s.replace(character,"",1))

            # Prepend the start character to each sub-permutation
            perms.extend(map(lambda x: character + x, sub_perms))

        return perms

# Given an input word, returns all permutations of the word found
# in the input dictionary
def findAnagrams(inputWord):
    # Start with an empty list of anagrams
    anagrams = list()

    # Get a list of permutations of the characters in the input word
    # Python already implements a method for permutations of iterables,
    # but I did roll my own recursive version at first (see above)
    #    perms = stringPermutations(inputWord)
    perms = list(''.join(p) for p in permutations(inputWord))
    perms.remove(inputWord)

    # anagrams is just the sublist of perms that returns true
    # on a call to dictionaryLookup()
    anagrams = list(p for p in perms if dictionaryLookup(p))
    # for p in perms:
    #     if dictionaryLookup(p) is True:
    #         anagrams.append(p)

    return anagrams

def main(words, dictFilename):
    # Read the words from our dictionary file into wordSet
    dictFile = open(dictFilename, 'r')
    global wordSet
    wordSet = set(strip_and_lower(w) for w in dictFile.read().splitlines())
    dictFile.close()

    # Find the anagrams for every string given as input to the script
    for w in words:
        # Print the word under scrutiny
        print(w, ": ", end="")

        # Find and print any anagrams it has in the supplied dictionary
        anagrams = findAnagrams(w)
        for a in anagrams:
            print(a, end=", ")

        # Get rid of the dangling ", " if necessary
        if len(anagrams) > 0:
            print("\b\b ", end="")
        print("")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Print the anagrams of input words.')
    parser.add_argument('words', metavar='W', type=str, nargs='+',
                   help='a word to find the anagrams of')
    parser.add_argument('-d', dest='dictionary',
                        default="/usr/share/dict/words",
            help='path to dictionary file (default: /usr/share/dict/words)')

    args = parser.parse_args()
    main(args.words, args.dictionary)
