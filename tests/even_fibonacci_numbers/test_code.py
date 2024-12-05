# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms.
# By starting with 1 and 2,
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci
# sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


from problems.even_fibonacci_numbers.code import fibonacci_even_sum


def test_fibonacci_10() -> None:
    assert fibonacci_even_sum(10) == 10


def test_fibonacci_34() -> None:
    assert fibonacci_even_sum(34) == 44


def test_fibonacci_1000() -> None:
    assert fibonacci_even_sum(1000) == 798


def test_fibonacci_100000() -> None:
    assert fibonacci_even_sum(100000) == 60696


def test_fibonacci_4000000() -> None:
    assert fibonacci_even_sum(4000000) == 4613732
