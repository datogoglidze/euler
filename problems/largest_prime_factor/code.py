# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def largest_prime_factor(n: int) -> int:
    prime_numbers = [
        potential_factor
        for potential_factor in range(2, int(n**0.5) + 1)
        if is_prime(potential_factor) and n % potential_factor == 0
    ]

    return prime_numbers[-1] if prime_numbers else n


def is_prime(number: int) -> bool:
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True
