
class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []

    def assign_department(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"


class Tutor(Teacher):

    def __init__(self, name, subject, department):
        super().__init__(name, subject)
        self.guided_department = department

    def send_message_from_parents(self, message):
        print(f"Wiadomość od rodziców wysłana: {message}")



def run_example():
    teacher = Teacher(name="Mikołaj", subject="Matematyka")
    teacher.assign_department("C1")
    print(f"Nauczyciel {teacher}")

    # Dostęp do pól i metod klasy bazowej z obiektu klasy potomnej
    tutor = Tutor(department="A2", name="Jakub", subject="Historia")
    print(f"Wychowawca nazywa się {tutor.name}")
    # tutor.assign_department("A1")
    # tutor.assign_department("B1")
    print(f"Wychowawca: {tutor}")
    tutor.send_message_from_parents(message="Pozdrowienia!")

if __name__ == "__main__":
    run_example()
