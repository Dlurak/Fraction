import math

class Fraction:
    def __init__(self, numerator: float, denominator: float):
        self.numerator = float(numerator)
        self.denominator = float(denominator)
        if self.denominator == 0:
            raise ZeroDivisionError

    def __add__(self, other):
        if type(other) == type(5) or type(other) == type(5.0): # check if other is an int or a float
            return Fraction(self.denominator * other + self.numerator, self.denominator)
        elif type(other) == type(Fraction(1, 1)):
            return Fraction(self.numerator*other.denominator + other.numerator*self.denominator, self.denominator*self.denominator)
        else:
            raise TypeError('can only concatenate fraction to int, float or fraction')

    def __mul__(self, other):
        if type(other) == type(int(5)) or type(other) == type(float(5.0)): # check if other is an int or float
            return Fraction(self.numerator * other, self.denominator)
        elif type(other) == type(Fraction(1, 2)): # check if other is an Fraction
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            raise TypeError('fractions can\'t be multiplyed with this type')

    def __sub__(self, other):
        if type(other) == type(Fraction(1, 2)):
            return Fraction(self.numerator*other.denominator-other.numerator*self.denominator, self.denominator*other.denominator)
        elif type(other) == type(5) or type(other) == type(5.0):
            return Fraction(self.numerator-self.denominator*other, self.denominator)
        else:
            raise TypeError

    def __div__(self, other):
        if type(other) == type(5) or type(other) == type(5.0):
            return Fraction(self.numerator, self.denominator*other)
        elif type(other) == type(Fraction(1, 2)):
            return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)
        else:
            raise TypeError

    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'


    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    def __int__(self):
        return int(self.numerator/self.denominator)
    def __float__(self):
        return self.numerator/self.denominator

    def reduce(self, value = None):
        if value == None:
            value = gcd(self.numerator, self.denominator)
        self.numerator /= value
        self.denominator /= value

    def expand(self, value: float):
        self.numerator *= value
        self.denominator *= value

    def inverse(self):
        numerator = self.numerator
        denominator = self.denominator
        self.numerator = denominator
        self.denominator = numerator

def gcd(a, b):
    r = a%b
    q = a//b
    if r == 0:
        gcd = b
    else:
        gcd = r
    while r != 0:
        a = b
        b = r
        gcd = r
        r = a%b
        q = a//b
    return gcd


def number_to_fraction(number):
    result = Fraction(number, 1)
    result.reduce()
    return result
