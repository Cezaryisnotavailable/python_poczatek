import csv

from estudent.student import Student

#
# def load_students_from_csv(file_name="students.csv"):
#     with open(file_name, newline="", encoding="utf-8") as students_file:
#         csv_reader = csv.reader(students_file)
#         students = []
#         for row_index, row in enumerate(csv_reader):
            # print(row)
            # print(f"{row_index}){','.join(row)}")
            # if row_index == 0:
            #     continue
            # grades_value = [int(value) for value in row[3].split(",")]
            # student = Student(first_name=row[0], last_name=row[1])
            # students.append(student)
            # for grade_value in grades_value:
            #     student.add_final_grade(grade_value)
            # student.promoted = str_to_bool(row[2])

    #         students.append(
    #             Student.from_csv(
    #                 first_name=row[0],
    #                 last_name=row[1],
    #                 promoted=str_to_bool(row[2]),
    #                 grades_values=grades_value
    #             )
    #         )

    # return students

def str_to_bool(str_bool):
    if str_bool == "True":
        return True
    elif str_bool == "False":
        return False
    raise ValueError(f" {str_bool} To niepoprawna wartość dla typu bool")


def load_students_from_csv(file_name="students.csv"):
    with open(file_name, newline="") as students_file:
        csv_reader = csv.reader(students_file)
        headers = next(csv_reader)
        return [
            Student.from_csv(
                first_name=row[0],
                last_name=row[1],
                promoted=str_to_bool(row[2]),
                grades_values=[int(value) for value in row[3].split(",")]
            )
            for row in csv_reader
        ]






