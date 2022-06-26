from estudent.school import create_school_with_students


def run_example():
    szkola = create_school_with_students("Hogwart")
    szkola.print_self()


if __name__ == "__main__":
    run_example()