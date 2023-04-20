#!/usr/bin/env python3
from random import randint, choice
from brain_games.cli import ask, get_answer, compare


SIGN = ['+', '-', '*']


def calc_game():

    i = 0
    while (i < 3):

        num1 = randint(0, 100)
        num2 = randint(0, 100)
        sign = choice(SIGN)

        ask(make_expression(num1, num2, sign))

        try:
            answer = int(get_answer())
        except ValueError:
            print("Error!")
            return False

        if compare(find_answer(num1, num2, sign), answer):
            i += 1
        else:
            return False
    return True


def make_expression(a, b, sign):

    return f"{a} {sign} {b}"


def find_answer(a, b, sign):

    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    else:
        return a * b
