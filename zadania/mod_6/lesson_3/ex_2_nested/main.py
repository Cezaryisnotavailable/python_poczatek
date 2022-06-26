from estudent.errors import LogicError, PlaceLimitError
from estudent.data_generator import generate_students
from estudent.grade_calculator import GradeCalculator
from estudent.school import School
from estudent.student import Student


def run_example():
    # student = Student(first_name="Bob", last_name="Bobowski")
    # try:
    #     print(student.grades_avg)
    # except LogicError as error:
    #     print(f"Błąd: {error}")

    students = generate_students(number_of_students=250)
    school = School(name="Mała", students=[])
    try:
        school.students = students
    except PlaceLimitError as error:
        print(f"Limit miejsc wynosi {error.places_limit}")








if __name__ == "__main__":
    run_example()