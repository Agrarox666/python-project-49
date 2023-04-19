#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user, ask, get_answer, compare, congrats


def main():

    name = welcome_user()

    if calc_game():
        congrats(name)
    else:
        return


def calc_game():

    print("What is the result of the expression?")
    i = 0
    while (i < 3):

        num1 = randint(0, 100)
        num2 = randint(0, 100)
        operation = randint(0, 2)

        ask(make_expression(num1, num2, operation))
        answer = int(get_answer())
        correct_answer = calc(num1, num2, operation)

        if compare(correct_answer, answer):
            i += 1
        else:
            return False
    return True


def make_expression(num1, num2, operation):

    sign = ['+', '-', '*']
    return f"{num1} {sign[operation]} {num2}"


def calc(a, b, operation):

    if operation == 0:
        return a + b
    elif operation == 1:
        return a - b
    else:
        return a * b


def addition(a, b):

    return a + b


def multiplication(a, b):

    return a * b


def subtraction(a, b):

    return a - b
