class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_sum = sum(sum(grades) for grades in self.grades.values())
        grades_count = sum(len(grades) for grades in self.grades.values())
        average_grade = grades_sum / grades_count if grades_count > 0 else 0
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def average_grade(self):
        grades_sum = sum(sum(grades) for grades in self.grades.values())
        grades_count = sum(len(grades) for grades in self.grades.values())
        return grades_sum / grades_count if grades_count > 0 else 0

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return False

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count

    def __str__(self):
        average_grade = self.average_grade()
        return (f"{super().__str__()}\n"
                f"Средняя оценка за лекции: {average_grade}")

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return False

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создание экземпляра студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

# Создание экземпляра лектора
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.grades['Python'] = [9, 8, 10]

# Создание экземпляра эксперта
cool_reviewer = Reviewer('Another', 'Person')
cool_reviewer.courses_attached += ['Python']

# Выставление оценок студенту
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Выставление оценок лектору от студента
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)

# Вывод информации о студенте
print(best_student)

# Вывод информации о лекторе
print(cool_lecturer)

# Вывод информации о проверяющем
print(cool_reviewer)

# Сравнение студентов
another_student = Student('Another', 'Student', 'your_gender')
another_student.courses_in_progress += ['Python']
another_student.grades['Python'] = [8, 9, 7]

print(best_student == another_student)  # Сравнение по средней оценке
print(best_student < another_student)   # Сравнение по средней оценке

# Сравнение лекторов
another_lecturer = Lecturer('Another', 'Lecturer')
another_lecturer.courses_attached += ['Python']
another_lecturer.grades['Python'] = [8, 9, 7]

print(cool_lecturer == another_lecturer)  # Сравнение по средней оценке
print(cool_lecturer < another_lecturer)   # Сравнение по средней оценке