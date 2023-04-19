#!/usr/bin/env python3
from brain_games.cli import welcome_user, congrats
from brain_games.games.even_game import even_game


def main():

    name = welcome_user()

    if even_game():
        congrats(name)
    else:
        return

if __name__ == '__main__':

    main()
