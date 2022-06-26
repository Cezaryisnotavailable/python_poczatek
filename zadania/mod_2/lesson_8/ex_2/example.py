import random

def say_hello():
    print("Hello World")


def say_goodbye():
    print("Goodbye!")


def randomize_func(first_func, second_func):
    number = random.randint(1, 2)
    if number == 1:
        return first_func
    return second_func


def run_example():
    hello_or_goodbye = randomize_func(say_hello, say_goodbye)
    hello_or_goodbye()


if __name__ == "__main__":
    run_example()