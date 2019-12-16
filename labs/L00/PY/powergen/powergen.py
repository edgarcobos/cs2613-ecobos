#!/usr/bin/python3

def powergen(n):
    count = 0
    while count < n * n:
        yield n ** count
        count = count + 1