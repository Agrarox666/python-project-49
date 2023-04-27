#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():

    task = randint(0, 100)
    correct_answer = str(task % 2 == 0 and 'yes' or 'no')
    return correct_answer, task
