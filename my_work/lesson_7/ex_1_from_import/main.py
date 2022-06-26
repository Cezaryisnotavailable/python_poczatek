from school import promotion_status
from school.grade_calculator import calculate_student_final_grades
from school.promote import check_promotion
from school.students_data import is_student_in_school



print("Witaj w elektronicznym dzienniku")

student_name = input("Podaj imię ucznia")

if not is_student_in_school(student_name):
    print(f"Niestety nie ma tego typa {student_name} na liście")
else:
    final_grades = calculate_student_final_grades(student_name)
    promotion_result = check_promotion(final_grades)

    if promotion_result == promotion_status.PASSED:
        print(f"Gratulacje! {student_name} zdał/a")
    elif promotion_result == promotion_status.FAILED:
        print(f"Niestety, {student_name} nie zdał/a")
    else:
        print("Upss, coś poszlo nie tak")