import random


def add_random_number_to_set(numbers):
    number = random.randint(0, 10)
    numbers.add(number)
    return numbers

def add_random_number_to_frozenset(numbers):
    number = random.randint(0, 10)
    return numbers.union({number})

def run_homework():
    # numbers = set()
    numbers = frozenset()
    while len(numbers) < 11:
        print(numbers)

        # numbers = add_random_number_to_set(numbers)
        # add_random_number_to_set(numbers)

        numbers = add_random_number_to_frozenset(numbers)
        # add_random_number_to_frozenset(numbers)

    print(numbers)

def run_homework_remember_result():
    numbers = frozenset()
    result = []

    while len(numbers) < 11:
        result.append(numbers)

        numbers = add_random_number_to_frozenset(numbers)
    print(result)
    print(numbers)


if __name__ == "__main__":
    run_homework_remember_result()
