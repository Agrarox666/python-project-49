#!/usr/bin/env python3
from random import randint

DESCRIPTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def is_prime(number):

    if (number < 2):
        return False
    i = 2
    while (i < number):
        if not (number % i):
            return False
        i += 1

    return True


def get_game():

    random_number = randint(0, 100)
    correct_answer =  is_prime(random_number) and 'yes' or 'no'
    return correct_answer, random_number
