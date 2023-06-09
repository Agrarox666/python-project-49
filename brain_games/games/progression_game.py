#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_game():

    begin = randint(0, 100)
    step = randint(1, 10)
    length = randint(5, 10)
    pass_member = randint(0, length - 1)

    x = 0
    member = begin
    task = ''

    while x < length:

        if (x == pass_member):
            task += '.. '
            x += 1
        else:
            member = begin + step * x
            task += str(member) + ' '
            x += 1

    correct_answer = find_progression(task)
    return correct_answer, task


def find_progression(progression):

    progression_list = progression.split(' ')
    pass_member = progression_list.index('..')

    if (pass_member == 0):
        step = int(progression_list[2]) - int(progression_list[1])
        return str(int(progression_list[1]) - step)

    elif (pass_member == 1):
        step = int(progression_list[3]) - int(progression_list[2])
        begin = int(progression_list[0])
    else:
        begin = int(progression_list[0])
        step = int(progression_list[1]) - int(progression_list[0])

    return str(begin + step * pass_member)
