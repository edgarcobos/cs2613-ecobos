from fizzbuzz import FizzBuzz

def test_fizzbuzz_next():
    fb=FizzBuzz(15)
    assert (list(fb) == [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz',
                        'Buzz', 11, 'Fizz', 13, 14,'FizzBuzz'])

def test_fizzbuzz_iter():
    fb=FizzBuzz(100)
    first = list(fb); second = list(fb)
    assert (first == second)