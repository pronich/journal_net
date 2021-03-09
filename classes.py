class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grade = {}

    def avg_grade(self):
        grade_list = []
        for k, v in self.grade.items():
            grade_list.append(sum(v) / (len(v)))
        avg_grade = round(sum(grade_list) / (len(grade_list)), 1)
        return avg_grade

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")


    def finished_course(self, course):
        if course in self.courses_in_progress:
            self.finished_courses += [course]
            self.courses_in_progress.remove(course)
        else:
            print(f'{self.name} не изучает {course}' )

    def estimate_lecture(self, lecture, course, grade):
        if not isinstance(lecture, Lecturer):
            print(f'Студент может оценить только лектора')
            return
        if course not in self.courses_in_progress:
            print(f'{self.name} не изучает {course} и не может его оценивать')
            return
        if course not in lecture.courses_list:
            print(f'{lecture.name} не преподает {course}')
            return
        else:
            if course not in lecture.grade:
                lecture.grade[course] = [grade]
            else:
                lecture.grade[course].append(grade)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_list = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade = {}

    def avg_grade(self):
        grade_list = []
        for k, v in self.grade.items():
            grade_list.append(sum(v) / (len(v)))
        avg_grade = round(sum(grade_list) / (len(grade_list)), 1)
        return avg_grade

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}")

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.avg_grade() > other.avg_grade()



class Reviewer(Mentor):
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")

    def estimate(self, student, course, grade):
        if course not in self.courses_list:
            print(f'{self.name} не оценивает {course}')
            return
        if course not in student.courses_in_progress:
            print(f'{student.name} не изучает {course}')
            return
        if not isinstance(student, Student):
            print(f'Ревьюер не может оценить преподавателя')
            return
        else:
            if course not in student.grade:
                student.grade[course] = [grade]
            else:
                student.grade[course].append(grade)
