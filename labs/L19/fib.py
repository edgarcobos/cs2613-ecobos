#!/usr/bin/python3
class Fib:
    def __init__(self,max):
        iter(self)
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        if self.a < self.max:
            temp = self.a
            self.a, self.b = self.b, self.a + self.b
            return temp
        else:
            raise StopIteration