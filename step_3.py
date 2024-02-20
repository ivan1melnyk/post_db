from step_1 import session, Student, Group, Teacher, Subject, Grade
from fill_data import generate_grades, generate_fake_data


def insert_data_to_db(students, groups, subjects, teachers, grades):

    for student in students:
        student = Student(name=student[1], group_id=student[2])
        session.add(student)

    for group in groups:
        group = Group(name=group[1])
        session.add(group)

    for teacher in teachers:
        # print('teacher', teacher[0], teacher[1])
        teacher = Teacher(name=teacher[1])
        session.add(teacher)
    session.commit()

    for subject in subjects:
        # print(subject, subject[2])
        subject = Subject(name=subject[1], teacher_id=subject[2])
        session.add(subject)
    session.commit()

    # print(len(grades))
    for grade in grades:
        grade = Grade(
            student_id=grade[0], subject_id=grade[1], grade=grade[2], date_received=grade[3])
        session.add(grade)
    session.commit()


if __name__ == "__main__":
    number_students = 50
    number_groups = 3
    number_subjects = 8
    number_teachers = 5

    students, groups, subjects, teachers = generate_fake_data(
        number_students, number_groups, number_subjects, number_teachers)
    grades = generate_grades(students, subjects)
    insert_data_to_db(students, groups, subjects, teachers, grades)
