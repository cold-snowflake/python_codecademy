import itertools
from classroom_organizer import ClassroomOrganizer

class_student = ClassroomOrganizer()
class_student_sorted = class_student.sorted_names
print(class_student_sorted)
for item in class_student_sorted:
    print(item)

class_student_sorted = iter(class_student_sorted)
for i in range(10):
    print(next(class_student_sorted))

print("-" * 50)
class_student_organize = class_student.student_organize()
for item in class_student_organize:
    print(item)

math_students = class_student.get_students_with_subject('Math')
science_students = class_student.get_students_with_subject('Science')
math_science_students = list(itertools.chain(math_students + science_students))
math_science_students_combinations = list(itertools.combinations(math_science_students, 4))
print(math_science_students_combinations)
