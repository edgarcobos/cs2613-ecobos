class FizzBuzz:
    def __init__(self, max=100):
        self.n = 1
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            temp = self.n
            if temp%3 == 0 and temp%5 == 0:
                temp = "FizzBuzz"
            elif temp%3 == 0:
                temp = "Fizz"
            elif temp%5 == 0:
                temp = "Buzz"
            self.n = self.n + 1
            return temp
        else:
            raise StopIteration