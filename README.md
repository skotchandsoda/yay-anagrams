# anagram.py
A Python 3 script for printing the anagrams of argument words.

It assumes that your dictionary file is at `/usr/share/dict/words`,
so if you're using a Unix-like operating system you're probably set.

Not all words files are created equal; Duke's CS department provides one
here: 

> `http://www.cs.duke.edu/~ola/ap/linuxwords` 

If you use an alternate dictionary file, pass the script the location of
that file via the `-d` option like this:

> `$ python3 anagram.py -d /path/to/dictionary/file`

Pass in the `-h` option for the standard usage printout.

### Examples

~~~
$ python3 anagram.py align
align: algin, langi, liang, linga

$ python3.3 anagram.py tree purple choke street
tree: teer, reet  
purple: pulper  
choke: 
street: retest, setter, tester
~~~
