#!/usr/bin/python3

from list2dict import list2dict, swapem

def test_empty():
    assert list2dict([]) == {}

def test_abc():
    dictionary=list2dict(["a", "b", "c"])
    assert dictionary == {1: 'a', 2: 'b', 3: 'c'}

def test_swap():
    dictionary=swapem(list2dict(["a", "b", "c"]))
    assert dictionary == {'a' :1, 'b' :2, 'c' :3}