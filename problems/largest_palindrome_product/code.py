# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome_product(n: int) -> int:
    largest_palindrome = 0

    for multiplier in range((10**n) - 1, 10 ** (n - 1) - 1, -1):
        for multiplicand in range(multiplier, 10 ** (n - 1) - 1, -1):
            product = multiplier * multiplicand

            if product < largest_palindrome:
                break

            if str(product) == str(product)[::-1]:
                largest_palindrome = product

    return largest_palindrome
