from classes import Student, Lecturer, Reviewer

def avg_grade_students(students, course):
    grade_list = []
    for student in students:
        if course in student.grade:
            grade_list.append(student.avg_course_grade(course))
        else: continue
    avg_grade = round(sum(grade_list)/len(grade_list), 1)
    return avg_grade

def avg_course_grade(lectures, course):
    grade_list = []
    for lecture in lectures:
        if course in lecture.grade:
            grade_list.append(lecture.avg_course_grade(course))
        else:
            continue
    avg_grade = round(sum(grade_list) / len(grade_list), 1)
    return avg_grade

# Создаем всех по 2
peter = Student('Peter', 'Parker', 'male')
peter.courses_in_progress += ['Python', 'JS', 'Git']
peter.grade['Git'] = [8, 10, 9, 7, 10]
peter.grade['Python'] = [10, 10]

sonya = Student('Sonya', 'Markova', 'female')
sonya.finished_courses += ['JS']
sonya.courses_in_progress += ['Python', 'Git']
sonya.grade['JS'] = [10, 10, 10, 10, 10]
sonya.grade['Python'] = [10, 10]
sonya.grade['Git'] = [9, 8, 7]

max = Lecturer('Maxim', 'Maximov')
max.courses_list.append('Python')
max.courses_list.append('English')
max.courses_list.append('Git')
max.grade['Python'] = [9]
max.grade['English'] = [10, 10]

john = Lecturer('John', 'Maximov')
john.courses_list.append('Python')
john.courses_list.append('English')
john.grade['Python'] = [10]
john.grade['English'] = [10, 10]

leon = Reviewer('Leon', 'Leonovich')
leon.courses_list += ['JS', 'English']

ada = Reviewer('Ada', 'Barova')
ada.courses_list += ['Python', 'English', 'Git']

# Выводим информацию по персонажам и изменениям с ними
print(f'-------------------------------------------------\nИзначальная информация по персонажам')
print(f'{peter}\n-----\n{sonya}\n-----\n{max}\n-----\n{john}\n-----\n{leon}\n-----\n{ada}')


peter.estimate_lecture(max, 'Git', 6)
sonya.estimate_lecture(max, 'Git', 8)
peter.estimate_lecture(john, 'Python', 9)
sonya.estimate_lecture(max, 'Python', 3)

leon.estimate(peter, 'JS', 5)
leon.estimate(sonya, 'English', 10)
ada.estimate(peter, 'Python', 8)
ada.estimate(sonya, 'Git', 6)

peter.finished_course('JS')

print(f'------\n{max > john}')

print(f'-------------------------------------------------\nИтоговая информация по персонажам')
print(f'{peter}\n-----\n{sonya}\n-----\n{max}\n-----\n{john}\n-----\n{leon}\n-----\n{ada}')

print(f'-------------------------------------------------\nСчитаем средние оценки')
print(avg_grade_students([peter, sonya], 'Git'))
print(f'-----')
print(avg_course_grade([max, john], 'Python'))