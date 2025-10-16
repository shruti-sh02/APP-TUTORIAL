def filter_students(criteria, students):
    return list(filter(criteria, students))

students = [
    {"name": "Amit", "cgpa": 8.5},
    {"name": "Riya", "cgpa": 7.9},
    {"name": "Vikram", "cgpa": 9.1},
]

filtered = filter_students(lambda s: s["cgpa"] > 8, students)
print(filtered)
