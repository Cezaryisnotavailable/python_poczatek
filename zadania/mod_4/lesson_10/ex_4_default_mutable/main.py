
from estudent.subject import Subject
from estudent.grade import Grade
from estudent.grade import FinalGrade

def run_example():

    math = Subject(identifier=1, name="Matematyka", is_obligatory=False)
    print(math)

    math.assign_teacher("Bob")
    math.assign_teacher("Alice")
    print(math)


if __name__ == "__main__":
    run_example()