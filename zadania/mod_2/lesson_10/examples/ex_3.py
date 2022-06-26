
def calculate_sum_via_args(*args):
    print(type(args))
    result = 0
    for number in args:
        result += number
    return result


def add_two_numbers(first, second):
    return first + second


def run_example():
    numbers = [1, 2, 3, 4, 5, 6]

    result = calculate_sum_via_args(*numbers)
    print(result)

    two_numbers = [10, 30]
    result = calculate_sum_via_args(*two_numbers)
    print(result)

    combined_numbers = [*numbers, *two_numbers]
    result = calculate_sum_via_args(*combined_numbers)
    print(result)


if __name__ == "__main__":
    run_example()