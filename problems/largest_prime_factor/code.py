# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def largest_prime_factor(n: int) -> int:
    lst = []

    for potential_factor in range(2, n + 1):
        if is_prime(potential_factor):
            lst.append(potential_factor)

    for prime in reversed(lst):
        if n % prime == 0:
            return prime


def is_prime(n: int) -> bool:
    for divisor in range(2, n):
        if n % divisor == 0:
            return False

    return True
