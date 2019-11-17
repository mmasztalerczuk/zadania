from highschool import Student, ClassRegister

student1 = Student()
student1.set_name("Ala")
student1.set_scores([1])

student2 = Student()
student2.set_name("Bob")
student2.set_scores([3])

dziennik_1 = ClassRegister(name="Klasa IVa")
dziennik_1.add_students(student1, student2)
dziennik_1.sort_students_by_mean()
dziennik_1.set_scores(Ala=[1,1,1], Bob=[3,2,1])
dziennik_1.print_student()

