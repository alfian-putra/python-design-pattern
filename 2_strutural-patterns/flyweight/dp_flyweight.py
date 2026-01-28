#!/usr/bin/python3

import sys


class Sentence:
    def __init__(self, sentence):
        self._mapWord = self.mapper(sentence)
        self._length= len(sentence.split())

    def mapper(self, sentence):
        word = sentence.split(" ")
        ls = {}
        c = 0
        for i in word:
            if not ls.get(i):
                ls[i] = []
            ls[i].append(c)
            c += 1
        return ls

    def __repr__(self):
        return repr(self._mapWord)
    def __str__(self):
        #pass
        s = ""
        for j in range(self._length):
          for i in self._mapWord:
              if j in self._mapWord[i]:
                  s += i + " "
                  break
        return s[:len(s)-1]

                    
        

print("The cat chased the mouse while the mouse tried to escape the cat.")
ex = Sentence("The cat chased the mouse while the mouse tried to escape the cat.")
print("Size Sentence() object : %s" % sys.getsizeof(ex))
print("Size str object : %s" % sys.getsizeof("The cat chased the mouse while the mouse tried to escape the cat."))
print(repr(ex))
print(ex)
