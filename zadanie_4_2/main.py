from highschool import *

student1 = Student()
student1.set_name("Ala")
student1.set_scores([1])

student2 = Student()
student2.set_name("Bob")
student2.set_scores([3])

dziennik_1 = ClassRegister(name="Klasa IVa")
dziennik_1.add_student(student1)
dziennik_1.add_student(student2)
dziennik_1.sort_students_by_mean()
dziennik_1.print_student()

