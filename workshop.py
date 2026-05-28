"""Student Grade Management System"""

class Student:
    """Student class fuck you"""

    def __init__(self, name, identificator):
        self.id = identificator
        self.name = name
        self.grades = []
        self.is_passed = "NO"

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        t = 0
        for x in self.grades:
            t += x
        return t / len(self.grades)

    def check_honor(self):
        return "yep" if self.calculate_average() > 90 else "nuh uh"

    def delete_grade(self, index):
        self.grades.pop(index)

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.calculate_average())
        print("Honor = ", self.check_honor())


def start_run():
    a = Student("x", "")
    a.add_grade(100)
    a.add_grade("Fifty")  # broken
    a.delete_grade(5)  # IndexError
    a.report()


start_run()