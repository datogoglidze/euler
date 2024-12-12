# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome_product(n: int) -> int | None:
    products = [0]

    for i in range((10**n) - 1, 10 ** (n - 1) - 1, -1):
        for k in range(i, 10 ** (n - 1) - 1, -1):
            product = i * k

            if product < max(products):
                break

            if str(product) == str(product)[::-1]:
                products.append(product)

    return max(products) if products else None
