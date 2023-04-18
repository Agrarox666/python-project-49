#!/usr/bin/env python3
from random import randint
import prompt


def main():

    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    i = 0
    while (i < 3):

        random_number = randint(0, 100)
        is_even = not (random_number % 2)
        if (is_even):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print("Question: " + str(random_number))
        answer = prompt.string("Your answer: ")

        if (answer == correct_answer):
            print("Correct!")
            i += 1
        else:
            print('\"' + answer + '\"' + 'is wrong answer ;(. Correct was \" ' + correct_answer + '\"')
            print('Let\'s try again!')
            return

    print("Congratulations!")


if __name__ == '__main__':

    main()
