from estudent import data_generator
from estudent.school import School
from estudent.grade import Grade



def run_example():
    students = data_generator.generate_students()

    students.sort(key=lambda student: student.grades_avg(), reverse=True)
    school = School("Hogwart", students)
    best_student = school.students[0]
    print(f"Oceny najlepszego ucznia to: {best_student.final_grades}")


if __name__ == '__main__':
    run_example()
