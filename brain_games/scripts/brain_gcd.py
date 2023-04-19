#!/usr/bin/env python3
from brain_games.cli import welcome_user, congrats
from brain_games.games.gcd_game import gcd_game


def main():

    name = welcome_user()

    if gcd_game():
        congrats(name)
    else:
        return


if __name__ == '__main__':

    main()
