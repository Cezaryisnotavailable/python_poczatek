from estudent.school import School
from estudent.config import Config

def grades_avg_for_student(student):
    return student.grades_avg()


def run_example():
    school = School.create_school_with_students("Hogwart")
    students = school.students

    students.sort(key=grades_avg_for_student)

    # print(school) # to samo się wypisze co z for na dole
    for student in students:
        print(student)




if __name__ == '__main__':
    run_example()
