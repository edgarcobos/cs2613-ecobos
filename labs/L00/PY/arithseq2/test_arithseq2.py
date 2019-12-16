from arithseq2 import arith_seq

def test_evens():
    assert arith_seq(0,2,10) == [0,2,4,6,8,10]

def test_odds():
    assert arith_seq(1,2,10) == [1,3,5,7,9]