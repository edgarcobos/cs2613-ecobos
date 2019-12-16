class ArithSeq:
    def __init__(self, first, step, max):
        self.first = first
        self.step = step
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.first <= self.max:
            temp = self.first
            self.first = self.first + self.step
            return temp
        else:
            raise StopIteration