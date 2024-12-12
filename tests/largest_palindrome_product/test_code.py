# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


from problems.largest_palindrome_product.code import largest_palindrome_product


def test_palindrome_for_2_digits() -> None:
    assert largest_palindrome_product(2) == 9009


def test_palindrome_for_3_digits() -> None:
    assert largest_palindrome_product(3) == 906609


def test_palindrome_for_4_digits() -> None:
    assert largest_palindrome_product(4) == 99000099
