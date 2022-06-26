
class Student:

    # Zadaniem konstruktora jest zdefiniowac i zainicjalizowac stan obiektu
    def __init__(self):
        self.first_name = "Mikołaj"
        self.last_name = "Lewandowski"
        self.age = 54


def run_example():
    student = Student()
    print(student.first_name)
    print(student.last_name)
    print(student.age)

    # Stan obiektu można zmodyfikować
    student.first_name = "Jakub"
    student.last_name = "Kowalski"
    student.age = 33
    print(student.first_name)
    print(student.last_name)
    print(student.age)



if __name__ == "__main__":
    run_example()