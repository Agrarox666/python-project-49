#!/usr/bin/env python3
from random import randint
from brain_games.cli import ask, get_answer, compare


def calc_game():

    i = 0
    while (i < 3):

        num1 = randint(0, 100)
        num2 = randint(0, 100)
        sign = random.choice(sign)

        ask(make_expression(num1, num2, sign))

        try:
            answer = int(get_answer())
        except ValueError:
            print("Error!")
            return False

        correct_answer = calc(num1, num2, sign)

        if compare(correct_answer, answer):
            i += 1
        else:
            return False
    return True


def make_expression(a, b, sign_num):

    sign = ['+', '-', '*']
    return f"{a} {random.choice(sign)} {b}"


def calc(a, b, sign):

    if sign == 0:
        return a + b
    elif sign == 1:
        return a - b
    else:
        return a * b
