# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome_product(n: int) -> int:
    products = []

    for i in range(10 ** (n - 1), int("9" * n) + 1):
        for k in range(10 ** (n - 1), int("9" * n) + 1):
            products.append(i * k)

    for i in sorted(products, reverse=True):
        prefix = str(i)[:n]
        suffix = str(i)[n:][::-1]

        if prefix == suffix:
            return i

    return -1
