#!/usr/bin/env python3
from brain_games.games.gcd_game import gcd_task, gcd_solution
from brain_games.game import run_game


def main():

    gcd_description = 'Find the greatest common divisor of given numbers.'
    run_game(gcd_task, gcd_solution, gcd_description)


if __name__ == '__main__':

    main()
