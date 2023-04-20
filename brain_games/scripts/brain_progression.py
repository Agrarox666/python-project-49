#!/usr/bin/env python3
from brain_games.games.progression_game import progression_task
from brain_games.games.progression_game import progression_solution
from brain_games.game import run_game


def main():

    progression_description = 'What number is missing in the progression?'
    run_game(progression_task, progression_solution, progression_description)


if __name__ == '__main__':

    main()
