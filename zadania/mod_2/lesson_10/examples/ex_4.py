
def print_grades(**kwargs):
    for subject, grade in kwargs.items():
        print(f"Z przedmiotu: {subject} wystawiono {grade}")

def run_example():

    grades = {
        "matematyka": 4,
        "fizyka": 4,
        "chemia": 5
    }

    print_grades(**grades)

    more_grades = {
        "polski": 3,
        "niemiecki": 1,
        "w-f": 6
    }

    all_grades = {**grades, **more_grades}
    print_grades(**all_grades)



if __name__ == "__main__":
    run_example()