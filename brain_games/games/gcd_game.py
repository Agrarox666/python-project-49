#!/usr/bin/env python3
from random import randint


def gcd_task():

    return f"{randint(0, 100)} {randint(0, 100)}"


def gcd_solution(numbers):

    list_numbers = numbers.split(' ')
    a, b = int(list_numbers[0]), int(list_numbers[1])

    if (b == 0):
        return str(a)
    else:
        return gcd_solution(f"{b} {a % b}")
