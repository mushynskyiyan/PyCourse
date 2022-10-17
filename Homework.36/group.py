class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
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


