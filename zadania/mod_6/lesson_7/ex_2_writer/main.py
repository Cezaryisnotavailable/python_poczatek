from estudent.data_generator import generate_students
from estudent.persistence import load_students_from_csv, save_students_as_csv


def run_example():
    students = generate_students(number_of_students=10)
    save_students_as_csv(students)


if __name__ == '__main__':
    run_example()
