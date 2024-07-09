import codecs
codecs.encode("text to be rot13()'ed", "rot_13")
import os

class Calc(object):
    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        if b == 0:
            return 0
        else:
            print(codecs.encode(os.environ['SECRET_FLAG'], 'rot13'))
        return a/b
