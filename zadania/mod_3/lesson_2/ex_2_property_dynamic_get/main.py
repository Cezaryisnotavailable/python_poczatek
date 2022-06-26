from estudent import data_generator
from estudent.school import School
from estudent.grade import Grade



def run_example():
    students = data_generator.generate_students()
    school = School("Hogwart", students)
    best_student = school.best_student
    print(f"Średnia z ocen najlepszego ucznia to: {best_student.grades_avg}")


if __name__ == '__main__':
    run_example()
