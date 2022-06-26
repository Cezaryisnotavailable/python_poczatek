from estudent import data_generator
from estudent.school import School
from estudent.grade import Grade



def run_example():
    students = data_generator.generate_students()
    school = School("Hogwart", students)
    print(school)

    new_students = data_generator.generate_students(number_of_students=8)
    school.students = new_students
    print(school)

    too_many_students = data_generator.generate_students(number_of_students=100)
    school.students = too_many_students
    print(school)


if __name__ == '__main__':
    run_example()
