# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# with no remainder by all of the numbers from 1 to 20?


from problems.smallest_multiple.code import smallest_multiple


def test_smallest_multiple_for_5() -> None:
    assert smallest_multiple(5) == 60


def test_smallest_multiple_for_7() -> None:
    assert smallest_multiple(7) == 420


def test_smallest_multiple_for_10() -> None:
    assert smallest_multiple(10) == 2520


def test_smallest_multiple_for_13() -> None:
    assert smallest_multiple(13) == 360360


def test_smallest_multiple_for_20() -> None:
    assert smallest_multiple(20) == 232792560
