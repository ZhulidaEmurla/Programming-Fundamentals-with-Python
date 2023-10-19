import math


num_students = int(input())
num_lectures = int(input())
additional_bonus = int(input())

max_bonus = -1
top_student_attendance = 0

for _ in range(num_students):
    student_attendance = int(input())

    bonus_points = (student_attendance / num_lectures) * (5 + additional_bonus)
    bonus_points = math.ceil(bonus_points)

    if bonus_points > max_bonus:
        max_bonus = bonus_points
        top_student_attendance = student_attendance

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {top_student_attendance} lectures.")
