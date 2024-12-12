# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def largest_prime_factor(n: int) -> int:
    prime_numbers = []

    for potential_factor in range(2, int(n**0.5) + 1):
        if is_prime(potential_factor):
            prime_numbers.append(potential_factor)

    for number in reversed(prime_numbers):
        if n % number == 0:
            return number

    return n


def is_prime(number: int) -> bool:
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True
