#!/usr/bin/env python3
from brain_games.cli import welcome_user, congrats, consolation
from brain_games.games.gcd_game import gcd_game


def main():

    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    if gcd_game():
        congrats(name)
    else:
        consolation(name)
        return


if __name__ == '__main__':

    main()
