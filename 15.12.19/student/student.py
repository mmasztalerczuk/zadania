class Student:
    def __init__(self, name="John", surname="Doe", gpa=0):
        self.name = name
        self.surname = surname
        self.gpa = gpa

    def set_first_name(self, name):
        self.name = name

    def get_first_name(self):
        return self.name

    def set_gpa(self, gpa):
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def set_surname(self, surname):
        self.surname = surname

    def get_surname(self):
        return self.surname

    def write_to_file(self, file_name):
        with open(file_name, "w") as fp:
            fp.write(self.name + "\n")
            fp.write(self.surname + "\n")
            fp.write(str(self.gpa) + "\n")

    @classmethod
    def load_from_file(cls, file_name):
        with open(file_name, "r") as fp:
            name, surname, gpa = [name.strip() for name in fp.readlines()]

        return cls(name, surname, int(gpa))
