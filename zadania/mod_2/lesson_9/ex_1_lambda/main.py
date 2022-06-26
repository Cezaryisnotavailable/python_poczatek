from estudent.school import School
from estudent.grade_calculator import GradeCalculator




def run_example():
    school = School.create_school_with_students("Hogwart")
    students = school.students
    for student in students:
        print(student)
    print("-" * 20)
    # funkcja anonimowa lambda, po lambda jest argument, który przyjmuje
    students.sort(key=lambda student: student.grades_avg())

    for student in students:
        print(student)






if __name__ == '__main__':
    run_example()
