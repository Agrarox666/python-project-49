#!/usr/bin/env python3
from random import randint, choice


SIGN = ['+', '-', '*']
DESCRIPTION = 'What is the result of the expression?'


def calc_expression(num1, num2, sign):


    if sign == '+':
        return str(num1 + num2)
    elif sign == '-':
        return str(num1 - num2)
    else:
        return str(num1 * num2)


def get_game():

    num1 = randint(0, 100)
    num2 = randint(0, 100)
    sign = choice(SIGN)

    task = f"{num1} {sign} {num2}"
    correct_answer = calc_expression(num1, num2, sign)

    return correct_answer, task
