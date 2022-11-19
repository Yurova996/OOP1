class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        ret = f'Имя: {self.name}\nФамилия: {self.surname}\n'

        if len(self.grades) > 0:
            ret += f'Средняя оценка за домашние задания: {self.average_grades()}\n'
        ret += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        ret += f'Заверешенные курсы: {", ".join(self.finished_courses)}\n'
        return ret














class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

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


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка: Или ревьюер не из того потока, или студент не учится на этом курсе')



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)