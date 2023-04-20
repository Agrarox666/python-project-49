#!/usr/bin/env python3
from random import randint


def even_task():

    return randint(0, 100)


def even_solution(number):

    if not (number % 2):
        return 'yes'
    else:
        return 'no'
