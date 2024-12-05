# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum
# of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


from problems.multiples_of_3_or_5.code import sums


def test_sum_10() -> None:
    assert sums(10) == 23


def test_sum_49() -> None:
    assert sums(49) == 543


def test_sum_1000() -> None:
    assert sums(1000) == 233168


def test_sum_19564() -> None:
    assert sums(19564) == 89301183
