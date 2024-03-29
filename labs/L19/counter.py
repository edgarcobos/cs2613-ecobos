class Counter:
    "Simulation of generator using only __next__ and __init__"
    def __init__(self,x):
        self.x = x
        self.first = x

    def __next__(self):
        if self.x == self.first:
            print('entering make_counter')
        else:
            print('incrementing x')
        self.x = self.x + 1
        return self.x - 1

print('first')
counter = Counter(100)
print('second')
print(next(counter))
print('third')
print(next(counter))
print('last')