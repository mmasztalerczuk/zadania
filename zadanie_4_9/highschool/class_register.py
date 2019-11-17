class ClassRegister:
    def __init__(self, name, teacher=None):
        self.name = name
        self.students = []
        self.teacher = teacher

    def __len__(self):
        len_stud = len(self.students)
        if self.teacher is not None:
            len_stud += 1
        return len_stud

    def add_student(self, student):
        self.students.append(student)

    def add_students(self, *students):
        self.students += students

    def sort_students_by_mean(self):
        self.students.sort()

    def compare_students(self, student_a, student_b):
        return student_a.mean < student_b.mean

    def print_student(self):
        for student in self.students:
            print(student.name, student.scores)

    def set_scores(self, **students):
        for name, scores in students.items():
            for student in self.students:
                if student.name == name:
                    student.set_scores(scores)
