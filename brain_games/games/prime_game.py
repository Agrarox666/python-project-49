#!/usr/bin/env python3
from random import randint
from brain_games.cli import ask, get_answer, compare


def prime_game():

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while (i < 3):

        task = randint(0, 100)
        ask(task)
        correct_answer = is_simple(task)

        answer = get_answer()
        if compare(correct_answer, answer):
            i += 1
        else:
            return False
    return True


def is_simple(number):

    if (number < 2):
        return 'yes'
    i = 2
    while (i < number):
        if not (number % i):
            return 'no'
        i += 1

    return 'yes'
