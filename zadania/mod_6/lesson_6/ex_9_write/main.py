import os


from estudent.data_generator import generate_students


def run_example():
    students = generate_students()

    students_data_file_path = os.path.join("data", "students.txt")
    with open(students_data_file_path, mode="w", encoding="utf-8") as students_file:
        for student in students:
            students_file.write(str(student))
            students_file.write("\n")

    new_student = generate_students()
    with open(students_data_file_path, mode="a", encoding="utf-8") as students_file:
        students_file.write("Jeszcze dodaliśmy: \n")
        for student in new_student:
            students_file.write(str(student))
            students_file.write("\n")







if __name__ == "__main__":
    run_example()