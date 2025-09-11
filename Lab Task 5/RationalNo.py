import math

class Rn:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        g = math.gcd(numerator, denominator)
        self.num = numerator // g
        self.den = denominator // g

    def __str__(self):
        return f"{self.num}/{self.den}"

    #  Find LCM 
    def lcm(self, a, b):
        return (a * b) // math.gcd(a, b)

    def __add__(self, other):
        lcm_den = self.lcm(self.den, other.den)
        new_n = self.num * (lcm_den // self.den) + other.num * (lcm_den // other.den)
        return Rn(new_n, lcm_den)

    def __sub__(self, other):
        lcm_den = self.lcm(self.den, other.den)
        new_n = self.num * (lcm_den // self.den) - other.num * (lcm_den // other.den)
        return Rn(new_n, lcm_den)

    def __mul__(self, other):
        new_n = self.num * other.num
        new_d = self.den * other.den
        return Rn(new_n, new_d)


# Test
p = Rn(2, 6)   # 1/3
q = Rn(2, 8)   # 1/4

print("p =", p)
print("q =", q)
print("p + q =", p + q)   # 7/12
print("p - q =", p - q)   # 1/12
print("p * q =", p * q)   # 1/12
