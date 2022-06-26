from estudent import data_generator
from estudent.grade_calculator import GradeCalculator
from estudent.school import School


def run_example():
    students = data_generator.generate_students(number_of_students=45)
    school = School(name="Mała szkoła", students=[])
    school.students = students


    student_avg = GradeCalculator.calculate_student_avg([])




if __name__ == "__main__":
    run_example()