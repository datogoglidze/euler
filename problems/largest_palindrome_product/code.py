# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome_product(n: int) -> int | None:
    products = {i * k for i in range(10 ** (n - 1), 10**n) for k in range(i, 10**n)}

    for product in sorted(products, reverse=True):
        if str(product) == str(product)[::-1]:
            return product

    return None
