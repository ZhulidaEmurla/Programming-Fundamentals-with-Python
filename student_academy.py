students_count = int(input())
students = {}

for _ in range(students_count):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

filtered_students = {name: sum(grades) / len(grades) for name, grades in students.items() if sum(grades) / len(grades) >= 4.5}

for name, average_grade in filtered_students.items():
    print(f"{name} -> {average_grade:.2f}")
