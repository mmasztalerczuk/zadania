class ClassRegister:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_students(self, *students):
        self.students += students

    def sort_students_by_mean(self):
        self.students.sort()

    def print_student(self):
        for student in self.students:
            print(student.name, student.scores)

    def set_scores(self, **students):
        for name, scores in students.items():
            for student in self.students:
                if student.name == name:
                    student.set_scores(scores)
