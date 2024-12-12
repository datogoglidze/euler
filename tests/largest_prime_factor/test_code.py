# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


from problems.largest_prime_factor.code import largest_prime_factor


def test_largest_for_2() -> None:
    assert largest_prime_factor(2) == 2


def test_largest_for_3() -> None:
    assert largest_prime_factor(3) == 3


def test_largest_for_5() -> None:
    assert largest_prime_factor(5) == 5


def test_largest_for_7() -> None:
    assert largest_prime_factor(7) == 7


def test_largest_for_8() -> None:
    assert largest_prime_factor(8) == 2


def test_largest_for_13195() -> None:
    assert largest_prime_factor(13195) == 29


def test_largest_for_600851475143() -> None:
    assert largest_prime_factor(600851475143) == 6857
