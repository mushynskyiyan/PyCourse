class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def __eq__(self, other):
        a = self.a/self.b
        b = other.a/other.b
        if a == b:
            return True
        else:
            return False

    def __gt__(self, other):
        a = self.a / self.b
        b = other.a / other.b
        if a > b:
            return True
        else:
            return False

    def __lt__(self, other):
        a = self.a / self.b
        b = other.a / other.b
        if a < b:
            return True
        else:
            return False

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)  # Fraction: 21, 18
f_d = f_b * f_a
print(f_d)  # Fraction: 6, 18
f_e = f_a - f_b
print(f_e)  # Fraction: 3, 18

print(f_d < f_c)  # True
print(f_d > f_e)  # True
print(f_a == f_b)  # False