class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()} {self.record_book}'


class Group:
    def __init__(self, number, max_students):
        self.number = number
        self.group = set()
        self.max_students = max_students

    def add_student(self, student):
        if len(self.group) >= gr.max_students:
            raise Exception('Baka Yaro!')
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)

    def find_student(self, last_name):
        for student in self.group:
            if last_name == str(student.last_name):
                return student
        return None

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students += f'{str(student)}\n'
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 33, 'Alex', 'AlexisSombrero', 'AN144')
st4 = Student('Male', 33, 'Luke', 'Skywalker', 'AN144')
st5 = Student('Male', 33, 'Dart', 'Wader', 'AN144')
st6 = Student('Male', 33, 'Master', 'Yoda', 'AN144')
st7 = Student('Male', 33, 'Emperor', 'Palpatin', 'AN144')
st8 = Student('Male', 33, 'Ernesto', 'Cheguevara', 'AN144')
st9 = Student('Male', 33, 'Marty', 'McFly', 'AN144')
st10 = Student('Male', 33, 'Obi-Wan', 'Kanobi', 'AN144')
st11 = Student('Male', 33, 'Mace', 'Windu', 'AN144')
gr = Group('PD1', 10)
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr)
print(gr.max_students)
try:
    gr.add_student(st11)
except Exception as e:
    print('BAKA!' + str(e))
print(gr)

