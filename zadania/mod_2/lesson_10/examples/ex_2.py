
def print_grades(**kwargs):
    print(type(kwargs))
    for subject, grade in kwargs.items():
        print(f"Z przedmiotu: {subject} wystawiono {grade}")


def run_example():
    print_grades(
        matematyka=4,
        fizyka=4
    )


if __name__ == "__main__":
    run_example()