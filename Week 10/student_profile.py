def student_profile(name):
    marks = {}

    def add_marks(subject, mark):
        marks[subject] = mark
        avg = sum(marks.values()) / len(marks)
        print(f"{name}'s updated average: {avg:.2f}")

    return add_marks

# Example
student = student_profile("Nikhil")
student("Math", 90)
student("Science", 80)
student("English", 85)
