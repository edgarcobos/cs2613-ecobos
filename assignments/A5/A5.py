#!/usr/bin/python3

from enum import Enum
import re

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

class Scanner:
    def __init__(self, code):
        '''initialize the values of pos and code for new objects'''
        self.pos = 0
        self.code = code
    
    def __iter__(self):
        '''sets pos to 0 and returns iterator'''
        self.pos = 0
        return self

    def __next__(self):
        '''uses regular expressions to match the various kinds of tokens and returns appropriate Token objects'''
        tok_regex = re.compile(r'(?P<IDENT>[A-Za-z_]+)|(?P<CURRENCY>-?\d+(\.\d*)?)|(?P<MISMATCH>[^\n \t]+)')
        search = tok_regex.search(self.code, self.pos)
        if search:
            kind = search.lastgroup
            value = search.group()
            if kind == 'IDENT':
                try:
                    kind = Type[value.upper()]
                except:
                    kind = Type.IDENT
            elif kind == 'CURRENCY':
                value = int(float(value) * 100) if '.' in value else int(value) * 100
                kind = Type.CURRENCY
            elif kind == 'MISMATCH':
                raise ValueError(value)
            temp = Token(kind, value)
            self.pos = search.end() + 1
            return temp
        else:
            raise StopIteration

def ledger(string):
    '''receives a string and returns a list of tuples or throws value error if unexpected token is found'''
    scanner = Scanner(string)

    dct = {}
    for token in scanner:
        if(token.type == Type.OPEN):
            kind = next(scanner).value
            val = next(scanner).value
            if kind not in dct:
                dct[kind] = val
            else:
                raise ValueError(token.value)
        elif(token.type == Type.TRANSFER):
            account = next(scanner).value
            recipient = next(scanner).value
            amount = next(scanner).value
            if account in dct and recipient in dct:
                dct[account] -= amount
                dct[recipient] += amount
            else:
                raise ValueError(token.value)
        elif(token.type == Type.IDENT):
            if token.value in dct:
                tup = (token.value, dct[token.value])
            else:
                tup = (token.value, 0)
            yield tup