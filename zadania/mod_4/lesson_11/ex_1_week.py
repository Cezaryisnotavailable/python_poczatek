from enum import Enum


class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def run_example():
    friday = Week.FRIDAY
    print(friday)
    print(friday.name, friday.value)

    print(friday is Week.FRIDAY)
    print(friday is Week.TUESDAY)

    print(Week(3))

    day_of_week_number = 4
    print(Week(day_of_week_number))

    day_of_week_from_name = Week["FRIDAY"]
    print(day_of_week_from_name)
    print(type(day_of_week_from_name))


if __name__ == '__main__':
    run_example()
