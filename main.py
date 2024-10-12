class User:
    def __init__(self, name, surname, email, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.__password_hash = None  # Приватна властивість

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def set_password(self, password):
        self.__password_hash = self._hash_password(password)

    def check_password(self, password):
        return self.__password_hash == self._hash_password(password)

    @staticmethod
    def _hash_password(password):
        # Простий хеш для прикладу (не використовувати в реальних системах)
        return hash(password)

class Mark:
    def __init__(self, subject, value, teacher):
        self.subject = subject
        self.value = value
        self.teacher = teacher  # Об'єкт вчителя, який виставив оцінку

    def __str__(self):
        return f"{self.subject}: {self.value} (виставив {self.teacher.full_name})"

class Student(User):
    def __init__(self, group_id, **kwargs):
        super().__init__(**kwargs)
        self.group_id = group_id
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_average_mark(self):
        if not self.marks:
            return 0
        total = sum(mark.value for mark in self.marks)
        return total / len(self.marks)

    def get_marks_by_subject(self, subject):
        return [mark for mark in self.marks if mark.subject == subject]

class Teacher(User):
    def __init__(self, subjects, **kwargs):
        super().__init__(**kwargs)
        self.subjects = subjects  # Список предметів

    def assign_mark(self, student, subject, value):
        if subject in self.subjects:
            mark = Mark(subject, value, self)
            student.add_mark(mark)
        else:
            print(f"{self.full_name} не викладає предмет {subject}")

class TeachingAssistant(Student, Teacher):
    def __init__(self, group_id, subjects, **kwargs):
        super().__init__(group_id=group_id, subjects=subjects, **kwargs)

    def assist_in_class(self):
        print(f"{self.full_name} асистує в класі.")

# Демонстраційний алгоритм роботи з класами

# Створення екземплярів
student1 = Student(
    name="Іван",
    surname="Петренко",
    email="ivan.petrenko@example.com",
    age=20,
    group_id=101
)

teacher1 = Teacher(
    name="Олена",
    surname="Коваль",
    email="olena.koval@example.com",
    age=35,
    subjects=["Математика", "Фізика"]
)

ta1 = TeachingAssistant(
    name="Марія",
    surname="Іваненко",
    email="maria.ivanenko@example.com",
    age=22,
    group_id=101,
    subjects=["Математика"]
)

# Робота з методами і властивостями
student1.set_password("studentpass")
teacher1.set_password("teacherpass")
ta1.set_password("tapass")

print(student1.full_name)  # Виведе: Іван Петренко
print(teacher1.full_name)  # Виведе: Олена Коваль
print(ta1.full_name)       # Виведе: Марія Іваненко

# Виклик методів
teacher1.assign_mark(student1, "Математика", 95)
teacher1.assign_mark(student1, "Фізика", 88)
ta1.assign_mark(student1, "Математика", 90)  # TA може ставити оцінки

print(f"Середня оцінка студента {student1.full_name}: {student1.get_average_mark()}")

# Виведення всіх оцінок студента
print(f"Оцінки студента {student1.full_name}:")
for mark in student1.marks:
    print(mark)

# Демонстрація поліморфізму
for person in [student1, teacher1, ta1]:
    print(f"{person.full_name} - Тип: {person.__class__.__name__}")

# Використання базових методів предметної області
ta1.assist_in_class()  # Виведе: Марія Іваненко асистує в класі.
