import math

class Fraction:
    def __init__(self, numerator: float, denominator: float):
        self.numerator = float(numerator)
        self.denominator = float(denominator)
        if self.denominator == 0:
            raise ZeroDivisionError

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

    def expanding(self, value: float):
        self.numerator *= value
        self.denominator *= value



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


var = Fraction(3.74543, 4)
var.reduce()
print(var)