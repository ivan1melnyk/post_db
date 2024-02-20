from my_select import select_list

headers_list = [['ID', 'Student Name', 'Grade'], ['ID', 'Student Name', 'Grade'], ['ID', 'Group Name', 'Grade'], ['Grade'], ['ID', 'Subject'],
                ['ID', 'Name'], ['ID', 'Student Name', 'Math Grade'], ['ID', 'Teacher Name', 'Math Grade'], ['ID', 'Subjects'], ['ID', 'Subject']]

select_goals = ['Знайти 5 студентів із найбільшим середнім балом з усіх предметів.',
                'Знайти студента із найвищим середнім балом з певного предмета.',
                'Знайти середній бал у групах з певного предмета.',
                'Знайти середній бал на потоці (по всій таблиці оцінок).',
                'Знайти які курси читає певний викладач.',
                'Знайти список студентів у певній групі.',
                'Знайти оцінки студентів у окремій групі з певного предмета.',
                'Знайти середній бал, який ставить певний викладач зі своїх предметів.',
                'Знайти список курсів, які відвідує певний студент.',
                'Список курсів, які певному студенту читає певний викладач.']


def create_table_with_headers(data, headers):
    header_line = "|".join(str(header).ljust(20) for header in headers)
    print(header_line)
    print("-" * len(header_line))

    for row in data:
        row_line = "|".join(str(cell).ljust(20) for cell in row)
        print(row_line)


for num, select in enumerate(select_list, 0):
    print('Select', num+1)
    print(select_goals[num])
    print('______________________________________________________________')
    data = select()
    try:
        create_table_with_headers(data, headers_list[num])
        # print(data)
    except:
        print(data)
    finally:
        print('\n')
