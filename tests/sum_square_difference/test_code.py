# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385. The square of the sum
# of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence, the difference between the sum
# of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640. Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum.


from problems.sum_square_difference.code import sum_square_difference


def test_sum_square_difference_for_10() -> None:
    assert sum_square_difference(10) == 2640


def test_sum_square_difference_for_20() -> None:
    assert sum_square_difference(20) == 41230


def test_sum_square_difference_for_100() -> None:
    assert sum_square_difference(100) == 25164150
