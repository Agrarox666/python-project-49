#!/usr/bin/env python3
from random import randint
from brain_games.cli import ask, get_answer, compare


def prime_game():

    i = 0
    while (i < 3):

        task = randint(0, 100)
        ask(task)

        if compare(is_simple(task), get_answer()):
            i += 1
        else:
            return False
    return True


def is_simple(number):

    if (number < 2):
        return 'no'
    i = 2
    while (i < number):
        if not (number % i):
            return 'no'
        i += 1

    return 'yes'
