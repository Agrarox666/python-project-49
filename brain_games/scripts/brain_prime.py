#!/usr/bin/env python3
from brain_games.games.prime_game import prime_task, prime_solution
from brain_games.game import run_game


def main():

    prime_description = ('Answer "yes" if given number is prime.'
                         'Otherwise answer "no".')
    run_game(prime_task, prime_solution, prime_description)


if __name__ == '__main__':

    main()
