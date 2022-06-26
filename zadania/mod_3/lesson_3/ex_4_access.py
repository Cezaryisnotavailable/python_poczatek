
class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []
        self.__private_info = "Dane prywatne klasy bazowej"

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

    def access_to_private_info(self):
        print(self.__private_info)

def run_example():



    tutor = Tutor(department="A2", name="Jakub", subject="Historia")

    tutor.access_to_private_info()

if __name__ == "__main__":
    run_example()
