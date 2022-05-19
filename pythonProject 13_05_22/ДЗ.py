# Реализовать класс для работы с обыкновенными дробями. Класс поддерживает все арифметические и логические операции.

# наибольший общий делитель

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


# класс простых дробей

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        if bottom == 0:
            print("знанаменатель не может быть равен 0")
            self.den = 1
        else:
            self.den = bottom

# строковый вид

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

# сложение

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# вычитание

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# умножение

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# деление

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

# равенство

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

# неравенство

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

# больше

    def __gt__(self, other):
        denominator = other.den * self.den
        firstnumerator = other.den * self.den / self.den * self.num
        secondnumerator = other.den * self.den / other.den * other.num

        return firstnumerator > secondnumerator

# меньше

    def __it__(self, other):
        denominator = other.den * self.den
        firstnumerator = other.den * self.den / self.den * self.num
        secondnumerator = other.den * self.den / other.den * other.num

        return firstnumerator < secondnumerator

# больше или равно

    def __ge__(self, other):
        denominator = other.den * self.den
        firstnumerator = other.den * self.den / self.den * self.num
        secondnumerator = other.den * self.den / other.den * other.num

        return firstnumerator >= secondnumerator

# меньше или равно

    def __le__(self, other):
        denominator = other.den * self.den
        firstnumerator = other.den * self.den / self.den * self.num
        secondnumerator = other.den * self.den / other.den * other.num

        return firstnumerator <= secondnumerator

x = Fraction(1, 2)
y = Fraction(2, 3)

print("сложение", x + y)
print("вычитание", x - y)
print("умножение", x * y)
print("деление", x/y)
print("равенство", x == y)
print("неравенство", x != y)
print("больше", x > y)
print("меньше", x < y)
print("больше или равно", x >= y)
print("меньше или равно", x <= y)