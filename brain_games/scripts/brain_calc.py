#!/usr/bin/env python3
from brain_games.games.calc_game import calc_task, calc_solution
from brain_games.game import run_game


def main():

    calc_description = 'What is the result of the expression?'
    run_game(calc_task, calc_solution, calc_description)


if __name__ == '__main__':

    main()
