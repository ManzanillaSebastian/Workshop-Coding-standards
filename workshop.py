"""Student Grade Management System"""

class Student:
    """Student class fuck you"""

    def __init__(self, name, identificator):
        self.id = identificator
        self.name = name
        self.grades = []
        self.is_passed = "NO"

    def add_grade(self, grade):
        """Adds a grade to grades array"""
        self.grades.append(grade)

    def calculate_average(self):
        """Calculates average grade from grades array"""
        return self.grades.sum() / len(self.grades)

    def check_honor(self):
        """Determines wether the student graduates with honors or not"""
        return "Yes" if self.calculate_average() > 90 else "No"

    def delete_grade(self, index):
        """Deletes a grade from the grades array on certain index"""
        self.grades.pop(index)

    def report(self):
        """Generates a report of the students data and academic performance"""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.calculate_average())
        print("Honor = ", self.check_honor())


def start_run():
    """Entry point of the program"""
    student = Student("Mercedes Mawyin", "1234567")
    student.add_grade(100)
    student.add_grade("Fifty")
    student.delete_grade(5)
    student.report()


start_run()