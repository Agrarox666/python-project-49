#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):

    return number % 2 == 0


def get_game():

    random_number = randint(0, 100)
    correct_answer = is_even(random_number) and 'yes' or 'no'
    return correct_answer, random_number
