#!/usr/bin/env python3
from random import randint
from brain_games.cli import ask, get_answer, compare


def even_game():

    i = 0
    while (i < 3):

        random_number = make_number()

        ask(str(random_number))

        if compare(find_answer(random_number), get_answer()):
            i += 1
        else:
            return False
    return True


def make_number():

    return randint(0, 100)


def find_answer(number):

    if not (number % 2):
        return 'yes'
    else:
        return 'no'
