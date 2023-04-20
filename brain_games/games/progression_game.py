#!/usr/bin/env python3
from random import randint


def progression_task():

    begin = randint(0, 100)
    step = randint(1, 10)
    length = randint(5, 10)
    pass_member = randint(0, length - 1)

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


def progression_solution(progression):

    progression_list = progression.split(' ')
    pass_member = progression_list.index('..')

    if (pass_member == 0):
        step = int(progression_list[2]) - int(progression_list[1]
        return int(progression_list[1]) - step 

    elif (pass_member == 1):
        step = int(progression_list[3]) - int(progression_list[2])
        begin = int(progression_list[0])
    else:
        begin = int(progression_list[0])
        step = int(progression_list[1]) - int(progression_list[0])

    return str(begin + step * pass_member)
