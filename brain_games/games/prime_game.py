#!/usr/bin/env python3
from random import randint


def prime_task():

    return randint(0, 100)


def prime_solution(number):

    if (number < 2):
        return 'no'
    i = 2
    while (i < number):
        if not (number % i):
            return 'no'
        i += 1

    return 'yes'
