#!/usr/bin/python3

from enum import Enum

class Type(Enum):
    BALANCE = 1
    CURRENCY = 2
    IDENT = 3
    OPEN = 4
    TRANSFER = 5

class Token:
    def __init__(self, type, value):
        '''initializes the values of type and value for new objects'''
        self.type = type
        self.value = value

    def __str__(self):
        '''returns objects, currency is "pretty printed" as dollars and cents'''
        if self.type.name == 'CURRENCY':
            return f'[{self.type.name}: {int(self.value)//100}.{int(self.value)%100}]'
        else:
            return f'[{self.type.name}: {self.value}]'

    def __eq__(self, other):
        '''checks if two token objects have the same attributes, case insensitive for our language keywords'''
        if isinstance(self, other.__class__):
            if self.type.name == 'IDENT' or self.type.name == 'CURRENCY':
                return vars(self) == vars(other)
            else:
                return self.type == other.type and self.value.lower() == other.value.lower()
        else:
            return NotImplemented