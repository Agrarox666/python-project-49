#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user, ask, get_answer, compare, congrats


def main():

    name = welcome_user()

    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    i = 0
    while (i < 3):

        random_number = randint(0, 100)
        is_even = not (random_number % 2)

        if (is_even):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        ask(str(random_number))
        answer = get_answer()

        if compare(correct_answer, answer):
            i += 1
        else:
            return

    congrats(name)


def generate_number():

    random_number = randint(0, 100)

if __name__ == '__main__':

    main()
