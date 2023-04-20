#!/usr/bin/env python3
from brain_games.cli import welcome_user, congrats, consolation
from brain_games.games.prime_game import prime_game


def main():

    name = welcome_user()

    if prime_game():
        congrats(name)
    else:
        consolation(name)
        return


if __name__ == '__main__':

    main()
