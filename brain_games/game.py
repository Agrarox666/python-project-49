import prompt


def run_game(game):

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print(game.DESCRIPTION)

    x = 0
    while (x < 3):

        correct_answer, task = game.game()
        print(f"Question: {task}")
        answer = prompt.string("Your answer: ")

        if (is_correct(correct_answer, answer)):
            x += 1
        else:
            print(f"Let's try again, {name}!")
            return False

    print(f"Congratulations, {name}!")
    return True


def is_correct(correct_answer, answer):

    try:
        if (correct_answer == answer):
            print("Correct!")
            return True
        else:
            wrong_answer(correct_answer, answer)
            return False

    except ValueError:
        wrong_answer(correct_answer, answer)
        return False


def wrong_answer(correct_answer, answer):

    print(f"\'{answer}\' is wrong answer ;(. "
          f"Correct answer was \'{correct_answer}\'")
