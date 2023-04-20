#!/usr/bin/env python3
from random import randint
from brain_games.cli import ask, get_answer, compare


def progression_game():

    i = 0
    while (i < 3):

        begin = randint(0, 100)
        step = randint(1, 10)
        length = randint(5, 10)
        pass_member = randint(0, length - 1)

        ask(make_progression(begin, step, length, pass_member))

        try:
            answer = int(get_answer())
        except ValueError:
            answer = None

        if compare(define_member(begin, step, pass_member), answer):
            i += 1
        else:
            return False
    return True


def make_progression(begin, step, length, pass_member):

    x = 0
    member = begin
    result = ''
    while x < length:

        if (x == pass_member):
            result += '.. '
            x += 1
        else:
            member = begin + step * x
            result += str(member) + ' '
            x += 1

    return result


def define_member(begin, step, pass_member):

    return begin + step * pass_member
