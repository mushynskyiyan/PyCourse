def add_one(lstnum):
    for i in range(len(lstnum)):
        lstnum[i] = str(lstnum[i])
    num = "".join(lstnum)
    required_num = int(num) + 1
    required_num = str(required_num)
    rlst =[]
    for i in range(len(required_num)):
        rlst.append(required_num[i])
    for i in range(len(rlst)):
        rlst[i] = int(rlst[i])
    return rlst


lstone = [1, 2, 3, 4]
print(add_one(lstone))

#Вариант с тем, чтобы пользователь ввел число, которое будет преобразовано в список, который будет передан в функцию.
#a = input("Enter number, we will do list from this number and give you another one: ")
#a = str(a)
#alst = []
#for i in range(len(a)):
#    alst.append(a[i])
#print(add_one(alst))