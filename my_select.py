from step_1 import session, Student, Grade, Group, Subject, Teacher
from sqlalchemy import func, desc, distinct


def select_1():
    return session.query(
        Student.id,
        Student.name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade, Student.id == Grade.student_id
           ).group_by(Student.id, Student.name
                      ).order_by(desc('avg_grade')
                                 ).limit(5
                                         ).all()


def select_2():
    return session.query(
        Student.id,
        Student.name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade, Student.id == Grade.student_id
           ).filter(Grade.subject_id == 1
                    ).group_by(Student.id, Student.name
                               ).order_by(desc('avg_grade')
                                          ).limit(1
                                                  ).all()


def select_3():
    return (
        session.query(
            Group.id,
            Group.name,
            func.avg(Grade.grade).label('avg_grade')
        )
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)  # Join with Grade table
        .filter(Grade.subject_id == 1)
        .group_by(Group.id, Group.name)
        .all()
    )


def select_4():
    return [float(session.query(func.avg(Grade.grade).label('average_grade')).scalar())]


def select_5():
    return session.query(
        Subject.id,
        Subject.name
    ).join(Teacher, Subject.teacher_id == Teacher.id
           ).filter(Teacher.id == 3
                    ).all()


def select_6():
    return session.query(
        Student.id,
        Student.name
    ).filter(Student.group_id == 3
             ).all()


def select_7():
    return session.query(
        Student.id,
        Student.name,
        Grade.grade
    ).join(Grade, Student.id == Grade.student_id
           ).filter(Student.group_id == 3, Grade.subject_id == 3
                    ).distinct(Student.id).all()


def select_8():
    return session.query(
        Teacher.id,
        Teacher.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Subject, Teacher.id == Subject.teacher_id
           ).join(Grade, Subject.id == Grade.subject_id
                  ).filter(Teacher.id == 2
                           ).group_by(Teacher.id, Teacher.name
                                      ).all()


def select_9():
    return session.query(
        Subject.id,
        Subject.name
    ).join(Grade, Subject.id == Grade.subject_id
           ).join(Student, Grade.student_id == Student.id
                  ).filter(Student.id == 5
                           ).distinct(Subject.id).all()


def select_10():
    return session.query(
        Subject.id,
        Subject.name
    ).join(Grade, Subject.id == Grade.subject_id
           ).join(Student, Grade.student_id == Student.id
                  ).join(Teacher, Subject.teacher_id == Teacher.id
                         ).filter(Student.id == 5, Teacher.id == 2
                                  ).distinct(Subject.id).all()


select_list = [select_1, select_2, select_3, select_4, select_5,
               select_6, select_7, select_8, select_9, select_10]
