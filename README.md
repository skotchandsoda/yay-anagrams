# anagram.py
A Python 3 script for printing the anagrams of argument words.

The script ignores the case of your input for sake of convenience.

It assumes that your dictionary file is at `/usr/share/dict/words`,
so if you're using a Unix-like operating system you're probably set.

Not all `words` files are created equal; Duke's CS department provides one
here: http://www.cs.duke.edu/~ola/ap/linuxwords

If you use an alternate dictionary file, pass the script the location of
that file via the `-d` option like this:

> `$ python3 anagram.py -d /path/to/dictionary/file`

In principle, dictionary files for languages other than English should
work, but this is untested.

Pass in the `-h` option for the standard usage printout.

### Examples

~~~
$ python3 anagram.py -h
usage: anagram.py [-h] [-d DICTIONARY] W [W ...]

Prints the case-insensitive anagrams of words.

positional arguments:
  W              word you want the anagrams for

optional arguments:
  -h, --help     show this help message and exit
  -d DICTIONARY  path to dictionary file (default: /usr/share/dict/words)

$ python3 anagram.py align
align: algin, langi, liang, linga

$ python3.3 anagram.py tree purple choke street
tree: teer, reet  
purple: pulper  
choke: 
street: retest, setter, tester
~~~
