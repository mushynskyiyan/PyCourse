def say_hi(name, age):
    hi = f"Hi. My name is {name} and I'm {age} years old"
    return hi


n = str(input("Enter name: "))
a = int(input("Enter age: "))
print(say_hi(n, a))
