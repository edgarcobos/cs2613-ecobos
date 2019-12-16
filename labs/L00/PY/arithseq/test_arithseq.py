from arithseq import ArithSeq

def test_evens():
    assert [ x for x in ArithSeq(0,2,10) ] == [0,2,4,6,8,10]

def test_odds():
    assert [ x for x in ArithSeq(1,2,10) ] == [1,3,5,7,9]

def test_empty():
    '''test empty sequence, none of the tests above assign a number greater than max to first'''
    assert [ x for x in ArithSeq(1, 2, 0) ] == []

def test_negative():
    '''test negative sequence, none of the tests above assign negative number to first'''
    assert [ x for x in ArithSeq(-10, 2, 0) ] == [-10,-8,-6,-4,-2,0]