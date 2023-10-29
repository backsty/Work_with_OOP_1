class Student:
    def __init__(self, name, surname):
        """Создаём метод __init__ для определения атрибутов класса Student"""
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_rating = float()

    def rate_hw(self, lecturer, course, grade):
        """Создаём метод с помощью которого студенты будут выставлять оценки своим лекторам"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    def __calcAvg__(self):
        """Создаём метод, который будет подсчитывать среднее значение лекторов за проведённые лекции"""
        grades_count = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
        avg_rating = sum(map(sum, self.grades.values())) / grades_count
        return avg_rating

    def __str__(self):
        """Создаём метод __str__ который реализует определение средней оценки и возвращает хар-ки экземпляра класса"""
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за домашнее задание: {self.__calcAvg__()}\n' \
                 f'Курсы в процессе обучения: {courses_in_progress_str}\n' \
                 f'Завершённые курсы: {finished_courses_str}'
        return result

    def __lt__(self, other):
        """Создаём метод, который сравнивает (через операторы сравнения) между собой лекторов по средней оценке
        за лекции и студентов по средней оценке за домашние задания."""
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.avg_rating < other.avg_rating


class Mentor:
    def __init__(self, name, surname):
        """Создаём метод __init__ для определения атрибутов класса Mentor"""
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Создаём метод __init__ для определения атрибутов дочернего класса Lecturer. main class - Mentor"""
    def __init__(self, name, surname):
        """Создаём метод __init__ для определения атрибутов дочернего класса Lecturer. main class - Mentor"""
        super().__init__(name, surname)
        self.grades = {}
        self.avg_rating = float()

    def __calcAvg__(self):
        """Создаём метод, который будет подсчитывать среднее значение лекторов за проведённые лекции"""
        grades_count = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
        avg_rating = sum(map(sum, self.grades.values())) / grades_count
        return avg_rating

    def __str__(self):
        """Данный метод возвращает хар-ки экземпляра класса"""
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.__calcAvg__()}'
        return result

    def __lt__(self, other):
        """Создаём метод, который сравнивает (через операторы сравнения) между собой лекторов по средней оценке
                за лекции и студентов по средней оценке за домашние задания."""
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.avg_rating < other.avg_rating


class Reviewer(Mentor):
    """Эксперты, проверяющие задания"""
    def rate_hw(self, student, course, grade):
        """Создаём метод, который считает рейтинг студентов по сделанным ими домашним работам"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Error"

    def __str__(self):
        """Создаём метод, который возвращает имя и фамилию проверяющего"""
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


# Создаём лекторов
best_lecturer_1 = Lecturer('Ivan', 'Bek')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Artem', 'Edwards')
best_lecturer_2.courses_attached += ['TypeScript']

best_lecturer_3 = Lecturer('Egor', 'Petrov')
best_lecturer_3.courses_attached += ['Python']

# Создаём проверяющих
cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['TypeScript']

cool_reviewer_2 = Reviewer('Evgeniy', 'Bender')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['TypeScript']

# Создаём студентов
student_1 = Student('Oleg', 'Tomas')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Max', 'Pavlov')
student_2.courses_in_progress += ['TypeScript']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Roman', 'Grin')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Оценки лекторов за лекции по имени курса
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 9)
student_1.rate_hw(best_lecturer_2, 'Python', 8)
student_1.rate_hw(best_lecturer_2, 'Python', 7)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 6)
student_1.rate_hw(best_lecturer_1, 'Python', 5)

student_2.rate_hw(best_lecturer_2, 'TypeScript', 10)
student_2.rate_hw(best_lecturer_2, 'TypeScript', 4)
student_2.rate_hw(best_lecturer_2, 'TypeScript', 5)

student_3.rate_hw(best_lecturer_3, 'Python', 9)
student_3.rate_hw(best_lecturer_3, 'Python', 10)
student_3.rate_hw(best_lecturer_3, 'Python', 3)

# Оценки студентов за дз
cool_reviewer_1.rate_hw(student_1, 'Python', 10)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)

cool_reviewer_2.rate_hw(student_2, 'TypeScript', 7)
cool_reviewer_2.rate_hw(student_2, 'TypeScript', 6)
cool_reviewer_2.rate_hw(student_2, 'TypeScript', 5)

cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)
cool_reviewer_2.rate_hw(student_3, 'Python', 10)
cool_reviewer_2.rate_hw(student_3, 'Python', 6)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)


print(f'Студенты:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

print(f'Лекторы:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

print(f'Результат сравнения студентов по средним оценкам за сделанные дз: '
      f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname} = '
      f'{student_1.__calcAvg__() > student_2.__calcAvg__()}')
print()

print(f'Результат сравнения лекторов по средним оценкам за лекции: '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = '
      f'{best_lecturer_1.__calcAvg__() < best_lecturer_2.__calcAvg__()}')
print()


# Создаём списки студентов и лекторов
student_list = [student_1, student_2, student_3]
best_lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


def students_rate(students_list, course_name):
    """Создаём функцию, которая будет считать средние оценки студентов за дз"""
    kol = 0
    summa = 0
    for student_hw in students_list:
        if student_hw.courses_in_progress == [course_name]:
            summa += student_hw.__calcAvg__()
            kol += 1
    avg_rating_all = summa / kol
    return avg_rating_all


def lecturer_rate(best_lecturer_list, course_name):
    """Создаём функцию, которая будет подсчитывать среднюю оценку лекторов за лекции"""
    kol = 0
    summa = 0
    for student_hw in best_lecturer_list:
        if student_hw.courses_attached == [course_name]:
            summa += student_hw.__calcAvg__()
            kol += 1
    avg_rating_all = summa / kol
    return avg_rating_all


print(f"Средняя оценка всех студентов по курсу {'Python'}: {students_rate(student_list, 'Python')}")
print()

print(f"Средняя оценка всех лекторов по курсу {'Python'}: {lecturer_rate(best_lecturer_list, 'Python')}")
print()
