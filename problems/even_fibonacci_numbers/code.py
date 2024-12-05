# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms.
# By starting with 1 and 2,
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci
# sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def fibonacci_even_sum(maximum_number: int) -> int:
    return sum([number for number in fibonacci(maximum_number) if number % 2 == 0])


def fibonacci(maximum_number: int) -> list[int]:
    numbers = [1, 2]

    while numbers[-1] <= maximum_number:
        numbers.append(numbers[-2] + numbers[-1])

    return numbers[:-1]
