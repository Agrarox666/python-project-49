#!/usr/bin/env python3
from brain_games.cli import welcome_user, congrats
from brain_games.games.calc_game import calc_game

def main():

    name = welcome_user()

    if calc_game():
        congrats(name)
    else:
        return

