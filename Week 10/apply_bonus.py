# Q1: Higher-order function for applying bonuses
def apply_bonus(func, salary):
    return func(salary)

def festival_bonus(salary):
    return salary + salary * 0.1

def performance_bonus(salary):
    return salary + salary * 0.2

# Example
print("Q1:", apply_bonus(performance_bonus, 50000))  # Output: 60000


# Q2: Filter students using criteria function
def filter_students(criteria, students):
    return list(filter(criteria, students))

students = [
    {"name": "Amit", "cgpa": 8.5},
    {"name": "Riya", "cgpa": 7.9},
    {"name": "Vikram", "cgpa": 9.1},
]

filtered = filter_students(lambda s: s["cgpa"] > 8, students)
print("Q2:", filtered)  # [{'name': 'Amit', 'cgpa': 8.5}, {'name': 'Vikram', 'cgpa': 9.1}]


# Q3: Generic operate function
def operate(func, a, b):
    return func(a, b)

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else None

# Example
print("Q3:", operate(mul, 5, 6))  # 30


# Q4: Nested function for student profile
def student_profile(name):
    marks = {}

    def add_marks(subject, mark):
        marks[subject] = mark
        avg = sum(marks.values()) / len(marks)
        print(f"{name}'s updated average: {avg:.2f}")

    return add_marks

# Example
print("Q4:")
student = student_profile("Nikhil")
student("Math", 90)
student("Science", 80)
student("English", 85)


# Q5: Discount calculator (function returning another function)
def discount_calculator(rate):
    def apply_discount(price):
        return price * (1 - rate)
    return apply_discount

# Example
ten_percent = discount_calculator(0.1)
print("Q5:", ten_percent(2000))  # 1800.0
