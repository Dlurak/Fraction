import exceptions


class Fraction:
    def __init__(self, fraction=None, numerator=None, denominator=None):
        if fraction == numerator == denominator is None:  # check if all 3 parameters are None
            raise TypeError('"Fraction" is missing either the arguments numerator and denominator or fraction.')
        if numerator is not None and denominator is not None:  # if numerator and denominator has values set the vars (fraction has lower priority)
            self.numerator = float(numerator)
            self.denominator = float(denominator)
        else:
            if isinstance(fraction, type(Fraction(numerator=1, denominator=2))):
                self.numerator = fraction.numerator
                self.denominator = fraction.denominator
            elif isinstance(fraction, type('')):
                values = fraction.split('/')
                if len(values) < 2:
                    raise exceptions.NoDivisionError('This string isn\'t a Division')
                elif len(values) > 2:
                    raise exceptions.ToManyValuesError('In this string are to many values for a division.')
                else:
                    try:
                        self.numerator = float(values[0])
                    except ValueError:
                        raise ValueError(f'The string {values[0]} can\'t be converted to an float.')
                    try:
                        self.denominator = float(values[1])
                    except ValueError:
                        raise ValueError(f'The string {values[1]} can\'t be converted to a float.')
            elif isinstance(fraction, (type([]), type(()))):
                if len(fraction) < 2:
                    raise exceptions.ToFewValuesError('A division need exactly 2 values')
                elif len(fraction) > 2:
                    raise exceptions.ToManyValuesError('A division need exactly 2 values')
                else:
                    try:
                        self.numerator = float(fraction[0])
                    except TypeError:
                        raise TypeError("can't convert this type to a float")
                    except ValueError:
                        raise ValueError(f'The value {fraction[0]} can\'t be converted to a float')

                    try:
                        self.denominator = float(fraction[1])
                    except TypeError:
                        raise TypeError("can't convert this type to a float")
                    except ValueError:
                        raise ValueError(f'The value {fraction[1]} can\'t be converted to a float')
            else:
                raise TypeError('With this type a fraction can\'t be produced')

        if self.denominator == 0:
            raise ZeroDivisionError

    def __add__(self, other):
        if isinstance(other, (type(1), type(1.0))):  # check if other is an int or a float
            return Fraction(numerator=self.denominator * other + self.numerator, denominator=self.denominator)
        elif isinstance(other, type(Fraction(numerator=1, denominator=2))):
            return Fraction(numerator=self.numerator * other.denominator + other.numerator * self.denominator,
                            denominator=self.denominator * other.denominator)
        else:
            raise TypeError('can only concatenate fraction to int, float or fraction')

    def __mul__(self, other):
        if type(other) == type(int(5)) or type(other) == type(float(5.0)):  # check if other is an int or float
            return Fraction(numerator=self.numerator * other,denominator= self.denominator)
        elif type(other) == type(Fraction(1, 2)):  # check if other is a Fraction
            return Fraction(numerator=self.numerator * other.numerator,denominator= self.denominator * other.denominator)
        else:
            raise TypeError('fractions can\'t be multiplied with this type')

    def __sub__(self, other):
        if type(other) == type(Fraction(1, 2)):
            return Fraction(numerator=self.numerator * other.denominator - other.numerator * self.denominator,denominator=self.denominator * other.denominator)
        elif type(other) == type(5) or type(other) == type(5.0):
            return Fraction(numerator=self.numerator - self.denominator * other,denominator= self.denominator)
        else:
            raise TypeError

    def __div__(self, other):
        if type(other) == type(5) or type(other) == type(5.0):
            return Fraction(numerator= self.numerator,denominator= self.denominator * other)
        elif type(other) == type(Fraction(1, 2)):
            return Fraction(numerator=self.numerator * other.denominator,denominator= self.denominator * other.numerator)
        else:
            raise TypeError

    def __repr__(self):
        return f'Fraction(numerator={self.numerator}, denominator={self.denominator})'

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __int__(self):
        return int(self.numerator / self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

    def reduce(self, value=None):
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
    r = a % b
    if r == 0:
        gcd = b
    else:
        gcd = r
    while r != 0:
        a = b
        b = r
        gcd = r
        r = a % b
    return gcd


def number_to_fraction(number):
    result = Fraction(fraction=[number, 1])
    result.reduce()
    return result
    