from powergen import powergen

def test_powergen():
    gen = powergen(2)
    first = next(gen)
    second = next(gen)
    third = next(gen)
    assert (first == 1)
    assert (second == 2)
    assert (third == 4)

def test_powergen_list():
    gen = powergen(3)
    threes = [n for n in gen]
    assert(threes == [1, 3, 9, 27, 81, 243, 729, 2187, 6561])