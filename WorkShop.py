"""Student Grade Management System."""


class Student:
    """Represents a student with grades and academic status."""

    def __init__(self, student_id, name):
        """Initialize a Student with ID, name, and empty grade list."""
        if not student_id or not name:
            raise ValueError("Student ID and name must not be empty.")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """Add a numeric grade (0–100) to the student record."""
        if not isinstance(grade, (int, float)) or not 0 <= grade <= 100:
            print(f"Invalid grade: {grade}. Must be a number between 0 and 100.")
            return
        self.grades.append(grade)

    def calc_average(self):
        """Return the average of all grades, or 0.0 if no grades exist."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Convert numeric average to a letter grade (A–F)."""
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def update_status(self):
        """Update pass/fail and honor roll flags based on current average."""
        avg = self.calc_average()
        self.is_passed = avg >= 60
        self.honor = avg >= 90

    def remove_grade_by_index(self, index):
        """Remove a grade by index; handles out-of-bounds gracefully."""
        if index < 0 or index >= len(self.grades):
            print(f"Index {index} is out of bounds.")
            return
        del self.grades[index]

    def remove_grade_by_value(self, value):
        """Remove first occurrence of a grade by value; handles missing value."""
        if value not in self.grades:
            print(f"Grade {value} not found.")
            return
        self.grades.remove(value)

    def report(self):
        """Print a formatted summary report for this student."""
        print("=" * 40)
        print(f"Student ID   : {self.student_id}")
        print(f"Name         : {self.name}")
        print(f"Grades (#)   : {len(self.grades)}")
        print(f"Average      : {self.calc_average():.2f}")
        print(f"Letter Grade : {self.get_letter_grade()}")
        print(f"Status       : {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor Roll   : {'Yes' if self.honor else 'No'}")
        print("=" * 40)


def start_run():
    """Entry point: demonstrate the Student system."""
    student = Student("S001", "Alice")
    student.add_grade(95.0)
    student.add_grade(88.5)
    student.add_grade(72.0)
    student.add_grade("Fifty")  # Invalid – will be rejected gracefully
    student.add_grade(-5)       # Invalid – will be rejected gracefully
    student.update_status()
    student.remove_grade_by_index(10)  # Out of bounds – handled gracefully
    student.remove_grade_by_value(72.0)
    student.report()


start_run()
