import student
import group


st1 = student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = student.Student('Male', 33, 'Alex', 'AlexisSombrero', 'AN144')
gr = group.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
print(gr)
gr.find_student('Jobs')
gr.find_student('Jobs2')
gr.delete_student('Jobs')
gr.delete_student('Alexi')
print(gr)