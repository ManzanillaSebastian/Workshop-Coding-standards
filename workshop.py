"""Student Grade Management System"""

def get_letter_grade(grade):
    """Maps the numerical grade to a letter"""
    if grade < 0.0 or grade > 100.0:
        raise ValueError
    if grade < 60.0:
        return "F"
    elif 60.0 <= grade < 70.0:
        return "D"
    elif 70.0 <= grade < 80.0:
        return "C"
    elif 80.0 <= grade < 90.0:
        return "B"
    elif 90.0 <= grade <= 100.0:
        return "A"

class Student:
    """Student class"""

    def __init__(self, name, identificator):
        self.id = identificator
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Adds a grade to grades array"""
        self.grades.append(grade)

    def calculate_average(self):
        """Calculates average grade from grades array"""
        return sum(self.grades) / len(self.grades)

    def is_passed(self, average_grade):
        """Determines if the student got approved or not"""
        return "Passed" if average_grade >= 60.0 else "Failed"

    def check_honor(self):
        """Determines wether the student graduates with honors or not"""
        return "Yes" if self.calculate_average() > 90 else "No"

    def delete_grade(self, index):
        """Deletes a grade from the grades array on certain index"""
        if index < 0 or index >= len(self.grades):
            raise IndexError
        self.grades.pop(index)

    def report(self):
        """Generates a report of the students data and academic performance"""
        average = self.calculate_average()
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + average)
        print("Letter Grade = ", get_letter_grade(average))
        print("Passed = ", self.is_passed(average))
        print("Honor = ", self.check_honor())


def main():
    """Entry point of the program"""
    try:
        student = Student("Mercedes Mawyin", "1234567")
        student.add_grade(100)
        student.add_grade("Fifty")
        student.delete_grade(5)
        student.report()
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    main()
