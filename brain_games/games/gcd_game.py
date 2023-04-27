#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game():

    task = f"{randint(0, 100)} {randint(0, 100)}"
    correct_answer = gcd_solution(task)

    return correct_answer, task


def gcd_solution(numbers):

    list_numbers = numbers.split(' ')
    a, b = int(list_numbers[0]), int(list_numbers[1])

    if (b == 0):
        return str(a)
    else:
        return gcd_solution(f"{b} {a % b}")
