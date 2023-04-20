#!/usr/bin/env python3
from random import randint, choice
from brain_games.cli import ask, get_answer, compare


SIGN = ['+', '-', '*']

def calc_task():

    num1 = randint(0, 100)
    num2 = randint(0, 100)
    sign = choice(SIGN)

    return f"{num1} {sign} {num2}"

def calc_solution(expression):

    list = expression.split(' ')
    a = int(list[0])
    b = int(list[2])
    sign = list[1]

    if sign == '+':
        return str(a + b)
    elif sign == '-':
        return str(a - b)
    else:
        return str(a * b)

