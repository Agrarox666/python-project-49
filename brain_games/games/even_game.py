#!/usr/bin/env python3
from random import randint
from brain_games.cli import ask, get_answer, compare


def even_game():

    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    i = 0
    while (i < 3):

        random_number = randint(0, 100)

        if not (random_number % 2):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        ask(str(random_number))
        answer = get_answer()

        if compare(correct_answer, answer):
            i += 1
        else:
            return False
    return True
