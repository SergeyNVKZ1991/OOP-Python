class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за Домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}

    def average_rate(self):
        self.average = round(sum(sum(self.grades1.values(), [])) / len(sum(self.grades1.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.average_rate()} '
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


Anna_student = Student('Anna', 'Ivanova', 'female')
Dima_student = Student('Dima', 'Borisov', 'Male')
Anna_student.finished_courses += ['Введение в программирование']
Anna_student.courses_in_progress += ['Python', 'Git']
Dima_student.finished_courses += ['Введение в программирование', 'GIT']
Dima_student.courses_in_progress += ['Python']

Ivan_mentor = Mentor('Ivan', 'Tsoy')
Katya_mentor = Mentor('Katya', 'Sidorova')

Anton_lecturer = Lecturer('Anton', 'Antonov')
Sonya_lecturer = Lecturer('Sonya', 'Smirnova')
Anton_lecturer.courses_attached += ['Python', 'Git']
Sonya_lecturer.courses_attached += ['Python', 'Git']

Mark_reviewer = Reviewer('Mark', 'Volkov')
Tanya_reviewer = Reviewer('Tanya', 'Kats')
Mark_reviewer.courses_attached += ['Python', 'Git']
Tanya_reviewer.courses_attached += ['Python', 'Git']

Anna_student.rate_lecturer(Anton_lecturer, 'Python', 9)
Anna_student.rate_lecturer(Sonya_lecturer, 'Phython', 7)
Dima_student.rate_lecturer(Anton_lecturer, 'Python', 10)
Anna_student.rate_lecturer(Sonya_lecturer, 'Python', 9)
Dima_student.rate_lecturer(Anton_lecturer, 'Python', 8)

Mark_reviewer.rate_hw(Anna_student, 'Python', 9)
Mark_reviewer.rate_hw(Dima_student, 'Python', 10)
Tanya_reviewer.rate_hw(Anna_student, 'Python', 10)
Tanya_reviewer.rate_hw(Anna_student, 'Python', 7)
Tanya_reviewer.rate_hw(Dima_student, 'Python', 9)
Mark_reviewer.rate_hw(Anna_student, 'Git', 8)

Anna_student.average_grade()
Dima_student.average_grade()
print(Anna_student < Dima_student)
print(Anna_student)
print(Dima_student)

Anton_lecturer.average_rate()
Sonya_lecturer.average_rate()
print(Anton_lecturer < Sonya_lecturer)
print(Anton_lecturer)
print(Sonya_lecturer)

print(Mark_reviewer)
print(Tanya_reviewer)

student_list = [Anna_student, Dima_student]


def grade_av_student(student_list, course):
    sum = 0
    count = 0
    for person in student_list:
        for i in person.grades[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


lecturer_list = [Anton_lecturer, Sonya_lecturer]


def grade_av_lecturer(lecturer_list, course):
    sum = 0
    count = 0
    for person in lecturer_list:
        for i in person.grades1[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


print(grade_av_student(student_list, 'Python'))
print(grade_av_lecturer(lecturer_list, 'Python'))