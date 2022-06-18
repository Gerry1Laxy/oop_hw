from random import randint


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, *courses):
        self.courses_in_progress += [*courses]
        for course in courses:
            self.grades[course] = []

    def estimate_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            lecturer.grades[course] += [grade]
        else:
            print('Error')

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        return (
            f'Имя: {self.name}'
            f'\nФамилия: {self.surname}'
            f'\nСредняя оценка за домашние задания: {self.get_average_grade():.2f}'
            f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
            f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        )

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() <= other.get_average_grade()
        else:
            return 'Not a student'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return 'Not a student'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        else:
            return 'Not a student'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses(self, *courses):
        self.courses_attached += [*courses]

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def add_courses(self, *courses):
        super().add_courses(*courses)
        for course in courses:
            self.grades[course] = []

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        return super().__str__() \
               + f'\nСредняя оценка за лекции: {self.get_average_grade():.2f}'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() <= other.get_average_grade()
        else:
            return 'Not a lecturer'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return 'Not a lecturer'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() <= other.get_average_grade()
        else:
            return 'Not a lecturer'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            student.grades[course] += [grade]
        else:
            return 'Error'


def average_grade(list_members, course):
    all_grades = []
    for member in list_members:
        if course in member.grades:
            all_grades += member.grades[course]
    return sum(all_grades) / len(all_grades)


if __name__ == '__main__':
    students = [
        Student('John', 'Small', 'M'),
        Student('Mary', 'Underwood', 'F')
    ]

    lecturers = [
        Lecturer('Mark', 'Newman'),
        Lecturer('Lewis', 'Johnston')
    ]
    reviewers = [
        Reviewer('Michael', 'Gardner'),
        Reviewer('Clifton', 'Henderson')
    ]

    students[0].add_courses('Python', 'C++')
    students[1].add_courses('Python', 'Git')
    for lecturer in lecturers:
        lecturer.add_courses('Python', 'Git')
    for reviewer in reviewers:
        reviewer.add_courses('Python', 'Git', 'C++')

    for reviewer in reviewers:
        for _ in range(randint(5, 10)):
            rand_student = students[randint(0, len(students) - 1)]
            reviewer.rate_hw(rand_student, 'Python', randint(1, 10))

    for student in students:
        for _ in range(randint(5, 10)):
            rand_lecturer = lecturers[randint(0, len(lecturers) - 1)]
            student.estimate_lecturer(rand_lecturer, 'Python', randint(1, 10))

    print('Студенты:')
    print(*students, sep='\n')
    print('Лекторы:')
    print(*lecturers, sep='\n')
    print('Ревьюеры:')
    print(*reviewers, sep='\n')

    print('Операторы сравнения:')
    print(students[0] > students[1])
    print(students[0] < students[1])
    print(students[1] == students[0])
    print(students[0] <= reviewers[1])
    print(lecturers[0] >= lecturers[1])
    print(lecturers[1] < lecturers[0])
    print(lecturers[0] != lecturers[1])

    print(
        'Средняя оценка по всем студентам на курсе Python: '
        f'{average_grade(students, "Python"):.2f}'
    )
    print(
        'Средняя оценка по всем лекторам на курсе Python: '
        f'{average_grade(lecturers, "Python"):.2f}'
    )
