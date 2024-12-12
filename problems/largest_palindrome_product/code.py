# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome_product(n: int) -> int:
    products = []

    for i in range(int("9" * n), pow(10, n - 1) - 1, -1):
        for k in range(int("9" * n), pow(10, n - 1) - 1, -1):
            products.append(i * k)

    for i in sorted(products, reverse=True):
        if str(i)[:n] == str(i)[n:][::-1]:
            return i

    return -1
