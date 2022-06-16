class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        return (sum(self.grades.values()) / len(self.grades.values()))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def add_course(self, course):
        self.courses_attached += [course]


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def add_course(self, course):
        super().add_course(course)
        self.grades[course] = []


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'


best_student = Student('Ruby', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'C++']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'C++']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'C++', 10)
cool_mentor.rate_hw(best_student, 'C++', 10)
cool_mentor.rate_hw(best_student, 'C++', 4)

print(best_student.grades)

student_john = Student('John', 'Small', 'M')
student_mary = Student('Mary', 'Underwood', 'F')

lecturer_mark = Lecturer('Mark', 'Newman')
lecturer_mark.add_course('Python')

student_john.courses_in_progress += ['Python']
student_mary.courses_in_progress += ['C++']

student_john.estimate_lecturer(lecturer_mark, 'Python', 10)
student_john.estimate_lecturer(lecturer_mark, 'Python', 10)
student_mary.estimate_lecturer(lecturer_mark, 'Python', 10)

print(lecturer_mark.__dict__)
print(student_john.__dict__)
print(student_mary.__dict__)
print(best_student.get_average_grade())
