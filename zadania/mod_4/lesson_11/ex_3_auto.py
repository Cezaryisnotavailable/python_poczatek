from enum import Enum, auto

class AutoName(Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values: list):
        return name


class Color(AutoName):
    BLUE = auto()
    GREEN = auto()
    RED = auto()


def run_example():
    blue = Color.BLUE
    green = Color.GREEN

    print(blue.name, blue.value)
    print(green.name, green.value)
    print(type(blue.name), type(blue.value))


if __name__ == '__main__':
    run_example()
