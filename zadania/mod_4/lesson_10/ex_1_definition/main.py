
from estudent.subject import Subject


def run_example():
    math = Subject(identifier=1, name="Matematyka", is_obligatory=True)
    print(math)


if __name__=="__main__":
    run_example()