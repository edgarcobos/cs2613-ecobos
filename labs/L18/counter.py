#!/usr/bin/python3

def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x = x + 1

def make_counter2(x):
    count = x
    def counter():
        nonlocal count
        if count == x:
            print('entering make_counter')
        count = count + 1
        return count - 1
    return counter
