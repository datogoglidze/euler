# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# with no remainder by all of the numbers from 1 to 20?


def smallest_multiple(n: int) -> int:
    number = n

    while True:
        is_divisible = True

        for i in range(1, n + 1):
            if number % i != 0:
                number += n
                is_divisible = False
                break

        if is_divisible:
            return number
