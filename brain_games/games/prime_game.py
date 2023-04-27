#!/usr/bin/env python3
from random import randint

DESCRIPTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def game():

    task = randint(0, 100)
    correct_answer = prime_solution(task)
    return correct_answer, task


def prime_solution(number):

    if (number < 2):
        return 'no'
    i = 2
    while (i < number):
        if not (number % i):
            return 'no'
        i += 1

    return 'yes'
