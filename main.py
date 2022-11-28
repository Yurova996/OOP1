from statistics import mean


class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades_by_course = list()
        self.student_list.append(self)

    def __str__(self):
        ret = f'Имя: {self.name}\nФамилия: {self.surname}\n'

        if len(self.grades) > 0:
            ret += f'Средняя оценка за домашние задания: {self.average_grades()}\n'
        ret += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        ret += f'Заверешенные курсы: {", ".join(self.finished_courses)}\n'
        return ret

    def average_grades(self):
        """Average of all grades"""
        for course, grades in self.grades.items():
            self.average_grades_by_course.append(round(mean(grades), 2))
            # self.average_grades_by_course.append(round(sum(grades) / len(grades), 2))
        return round(mean(self.average_grades_by_course), 2)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка: Либо студент не учится на этом курсе, либо лектор этот курс не ведет')

    def av(self, student, course):
        """Считаем среднии оценки по курсу"""
        if isinstance(student, Student) and course in student.grades:
            return round(mean(student.grades[course]), 2)

    def __lt__(self, other):
        if isinstance(other, Student):
            print(f"Сравнение студентов: {other.name} {other.surname} и {self.name} {self.surname}")
            for other_course, other_values in other.grades.items():
                for self_course, self_values in self.grades.items():
                    if other_course == self_course:
                        if self.av(other, other_course) > self.av(self, self_course):
                            print(f'По {other_course} {other.name} {other.surname} лучше {self.name} {self.surname}')
                        else:
                            print(f'По {other_course} {self.name} {self.surname} лучше {other.name} {other.surname}')
        else:
            return 'this is not a Student'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        ret = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        if hasattr(self, 'courses_attached') and len(self.courses_attached) > 0:
            ret += f'Ведёт следующие курсы: {",  ".join(self.courses_attached)}\n'
        return ret


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lecturer_list.append(self)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            print(f"Сравнение лекторов: {other.name} {other.surname} и {self.name} {self.surname}")
            for other_course, other_values in other.grades.items():
                for self_course, self_values in self.grades.items():
                    if other_course == self_course:
                        if self.average_grades(other, other_course) > self.average_grades(self, self_course):
                            print(f'По {other_course} {other.name} {other.surname} лучше {self.name} {self.surname}')
                        else:
                            print(f'По {other_course} {self.name} {self.surname} лучше {other.name} {other.surname}')
        else:
            return 'this is not a Lecturer'

    def average_grades(self, lecturer, course):
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            return round(mean(lecturer.grades[course]), 2)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка: Или ревьюер не из того потока, или студент не учится на этом курсе')

stud1 = Student('Иван', 'Иванов', 'male')
stud1.courses_in_progress += ['Python', 'Java', 'Git']
stud1.finished_courses += ('Введение в программирование', 'Английский для программистов')

stud2 = Student('Пётр', 'Петров', 'male')
stud2.courses_in_progress += ['Python', 'Git']
stud2.finished_courses.append('Введение в программирование')

print(stud1, stud2, sep="\n")


print('Создали Лекторов')
lect1 = Lecturer('Виктор', 'Викторов')
lect1.courses_attached += ['Python', 'Git', 'Введение в программирование']

lect2 = Lecturer('Марина', 'Мариновна')
lect2.courses_attached += ['Java', 'Git', 'Введение в программирование']

print(lect1, lect2, sep="\n")


print('Создали Ревьюеров')
rev1 = Reviewer('Альберт', 'Альбертов')
rev1.courses_attached += ['Python', 'Git']

rev2 = Reviewer('Илларион', 'Илларионов')
rev2.courses_attached += ['Python']

print(rev1, rev2, sep="\n")

print('Ревьюеры оценили работы студентов')
rev1.rate_hw(stud1, 'Python', 1)
rev1.rate_hw(stud1, 'Python', 7)
rev1.rate_hw(stud1, 'Python', 9)
rev1.rate_hw(stud1, 'Python', 4)
rev1.rate_hw(stud1, 'Git', 10)
rev1.rate_hw(stud1, 'Git', 10)
rev1.rate_hw(stud1, 'Git', 9)

rev2.rate_hw(stud2, 'Python', 1)
rev2.rate_hw(stud2, 'Python', 10)
rev2.rate_hw(stud2, 'Python', 4)
rev2.rate_hw(stud2, 'Python', 7)


print("Студенты оценили лекции лекторов")
stud1.rate_lecturer(lect1, 'Python', 8)
stud2.rate_lecturer(lect1, 'Python', 9)
stud1.rate_lecturer(lect1, 'Java', 10)
stud2.rate_lecturer(lect1, 'Java', 9)
stud1.rate_lecturer(lect1, 'Git', 5)
stud2.rate_lecturer(lect1, 'Git', 4)

stud1.rate_lecturer(lect2, 'Python', 1)
stud2.rate_lecturer(lect2, 'Python', 1)
stud1.rate_lecturer(lect2, 'Java', 7)
stud2.rate_lecturer(lect2, 'Java', 9)
stud1.rate_lecturer(lect2, 'Git', 8)
stud2.rate_lecturer(lect2, 'Git', 10)

print('Выводим студентов')
print(stud1, stud2, sep="\n")

stud1 > stud2
stud2 > stud1

print('Выводим лекторов')
print(lect1, lect2, sep="\n")

print('Сравниваем лекторов')
lect1 > lect2
lect2 > lect1


print('Четвертое задание')


def students_average_grades_by_course(students, course):
    av = []
    for student in students:
        av.append(mean(student.grades[course]))
    return round(mean(av), 2)


def lecturers_average_grades_by_course(lecturers, course):
    av = []
    for lecturer in lecturers:
        av.append(mean(lecturer.grades[course]))
    return round(mean(av), 2)


course = "Python"
print(f'Средняя оценка у студентов по {course} = {students_average_grades_by_course(Student.student_list, course)}')
course = "Git"
print(f'Средняя оценка у лекторов по {course} = {lecturers_average_grades_by_course(Lecturer.lecturer_list, course)}')

