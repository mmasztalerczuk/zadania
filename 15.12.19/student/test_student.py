import os
import unittest
from .student import Student


class TestStudent(unittest.TestCase):
    file_name = "test.txt"

    def setUp(self) -> None:
        if os.path.isfile(TestStudent.file_name):
            os.remove(TestStudent.file_name)

    def tearDown(self) -> None:
        if os.path.isfile(TestStudent.file_name):
            os.remove(TestStudent.file_name)

    def test01_simple_test(self):
        # given
        student = Student()

        # then
        self.assertEqual("John", student.get_first_name())
        self.assertEqual("Doe", student.get_surname())
        self.assertEqual(0, student.get_gpa())

    def test02_set_name(self):
        # given
        name = "ala"
        student = Student(name=name)

        # then
        self.assertEqual(name, student.get_first_name())
        self.assertEqual("Doe", student.get_surname())
        self.assertEqual(0, student.get_gpa())

    def test03_set_surname(self):
        # given
        surname = "kot"
        student = Student(surname=surname)

        # then
        self.assertEqual("John", student.get_first_name())
        self.assertEqual(surname, student.get_surname())
        self.assertEqual(0, student.get_gpa())

    def test04_set_gpa(self):
        # given
        gpa = 13
        student = Student(gpa=gpa)

        # then
        self.assertEqual("John", student.get_first_name())
        self.assertEqual("Doe", student.get_surname())
        self.assertEqual(gpa, student.get_gpa())

    def test05_setters(self):
        # given
        name = "ala"
        surname = "kot"
        gpa = 311

        # when
        student = Student()
        student.set_first_name(name)
        student.set_surname(surname)
        student.set_gpa(gpa)

        # then
        self.assertEqual(name, student.get_first_name())
        self.assertEqual(surname, student.get_surname())
        self.assertEqual(gpa, student.get_gpa())

    def test06_write_to_file(self):
        # given
        name = "ala"
        surname = "kot"
        gpa = 311

        # when
        student = Student()
        student.set_first_name(name)
        student.set_surname(surname)
        student.set_gpa(gpa)

        student.write_to_file(TestStudent.file_name)

        # then
        with open(TestStudent.file_name) as fp:
            data = fp.readlines()

        self.assertEqual([name + "\n", surname + "\n", str(gpa) + "\n"], data)

    def test07_load_from_file(self):
        # given
        name = "ala"
        surname = "kot"
        gpa = 311

        # when
        student = Student()
        student.set_first_name(name)
        student.set_surname(surname)
        student.set_gpa(gpa)

        student.write_to_file(TestStudent.file_name)

        new_student = Student.load_from_file(TestStudent.file_name)

        self.assertEqual(name, new_student.get_first_name())
        self.assertEqual(surname, new_student.get_surname())
        self.assertEqual(gpa, new_student.get_gpa())
