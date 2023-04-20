#!/usr/bin/env python3
from brain_games.games.even_game import even_task, even_solution
from brain_games.game import run_game


def main():

    even_description = 'Answer "yes" if the number is even,' \
                       ' otherwise answer "no".'
    run_game(even_task, even_solution, even_description)


if __name__ == '__main__':

    main()
