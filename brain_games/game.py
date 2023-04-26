import prompt


def run_game(game_task, game_solution, game_description):

    name = welcome_user()
    print(game_description)

    x = 0
    while (x < 3):

        task = game_task()
        ask(task)
        answer = get_answer()

        if (is_correct(game_solution(task), answer)):
            x += 1
        else:
            consolation(name)
            return False

    congrats(name)
    return True


def welcome_user():

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")

    return name


def ask(task):

    print(f"Question: {task}")


def get_answer():

    answer = prompt.string("Your answer: ")
    return answer


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


def congrats(name):

    print(f"Congratulations, {name}!")


def consolation(name):

    print(f"Let's try again, {name}!")


def wrong_answer(correct_answer, answer):

    print(f"\'{answer}\' is wrong answer ;(. "
          f"Correct answer was \'{correct_answer}\'")
