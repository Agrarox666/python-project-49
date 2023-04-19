#!/usr/bin/env python3
from random import randint
from brain_games.cli import ask, get_answer, compare


def gcd_game():

    print("Find the greatest common divisor of given numbers.")
    i = 0
    while (i < 3):

        random_number1 = randint(0, 100)
        random_number2 = randint(0, 100)
        correct_answer = find_gcd(random_number1, random_number2)

        ask(f"{random_number1} {random_number2}")
        try:
            answer = int(get_answer())
        except ValueError:
            print("Error!")
            return False

        if compare(correct_answer, answer):
            i += 1
        else:
            return False
    return True


def find_gcd(a, b):

    if (b == 0):
        return a
    else:
        return find_gcd(b, a % b)
