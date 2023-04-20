#!/usr/bin/env python3
from brain_games.cli import welcome_user, congrats, consolation
from brain_games.games.calc_game import calc_game


def main():

    name = welcome_user()
    print("What is the result of the expression?")

    if calc_game():
        congrats(name)
    else:
        consolation(name)
        return


if __name__ == '__main__':

    main()
