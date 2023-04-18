import prompt


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


def compare(correct_answer, answer):

    if(correct_answer == answer):
        print("Correct!")
        return True
    else:
        print(f"\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'")
        return False


def congrats(name):

    print(f"Congratulations, {name}!")
