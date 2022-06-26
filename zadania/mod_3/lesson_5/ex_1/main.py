from estudent import data_generator
from estudent.school import School
from estudent.grade import Grade



def run_example():
    students = data_generator.generate_students()
    print(students.first_student)


if __name__ == '__main__':
    run_example()
