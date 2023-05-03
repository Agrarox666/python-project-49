import prompt


def run_game(game):

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print(game.DESCRIPTION)

    rounds = 0
    while (rounds < 3):

        correct_answer, task = game.get_game()
        print(f"Question: {task}")
        answer = prompt.string("Your answer: ")

        if (correct_answer == answer):
            print("Correct!")
            rounds +=1
        else:
            print(f"\'{answer}\' is wrong answer ;(. "
                  f"Correct answer was \'{correct_answer}\'"
                  f"\nLet's try again, {name}!")
            return False

    print(f"Congratulations, {name}!")
    return True
