#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(numbers):

    list_numbers = numbers.split(' ')
    num1, num2 = int(list_numbers[0]), int(list_numbers[1])

    if not num2:
        return str(num1)
    else:
        return find_gcd(f"{num2} {num1 % num2}")


def get_game():

    task = f"{randint(0, 100)} {randint(0, 100)}"
    correct_answer = find_gcd(task)

    return correct_answer, task
