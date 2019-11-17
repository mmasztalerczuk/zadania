from highschool import Student, ClassRegister, Teacher


student1 = Student()
student1.set_name("Ala")
student1.set_scores([1])

student2 = Student()
student2.set_name("Bob")
student2.set_scores([3])

dziennik_1 = ClassRegister(name="Klasa IVa", teacher=Teacher())
dziennik_1.add_students(student1, student2)
dziennik_1.sort_students_by_mean()
dziennik_1.set_scores(Ala=[1,1,1], Bob=[3,2,1])
dziennik_1.print_student()

n = [student1, student2]
print(dziennik_1.compare_students(*n))

n = {"student_a": student2, "student_b": student1}
print(dziennik_1.compare_students(**n))

print(len(dziennik_1))

