import pprint
class Student:
    students = {}
    n = 0

    def __init__(self, roll_no, name, age) -> None:
        self.r = roll_no
        self.n = name
        self.a = age
        Student.n += 1
        Student.students[Student.n] = {self.r, self.n, self.a}

    def display(self):
        print(f'Roll No: {self.r}, Name: {self.n}, Age: {self.a}')
    def get_list(self):
        return Student.students

s1 = Student(1, 'Katuri Akash', 21)
s2 = Student(1, 'Katuri ak', 21)
s3 = Student(1, 'Katuri kash', 21)
s3 = Student(1, 'Katuri kash', 21)
s3 = Student(1, 'Katuri kash', 21)
s3 = Student(1, 'Katuri kash', 21)
s3 = Student(1, 'Katuri kash', 21)
s=Student.students
pprint.pprint(s)