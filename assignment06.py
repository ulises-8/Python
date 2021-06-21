"""
CS3B, Assignment #6, Complex Numbers
Ulises Marian
"""
import math
from functools import total_ordering
import copy

@total_ordering
class Complex:
    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return f"({self.real}, {self.imag})"

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        if not (hasattr(real, "__int__") or hasattr(real, "__float__")):
            raise TypeError("value must be a number")
        self._real = real

    @property
    def imag(self):
        return self._imag

    @imag.setter
    def imag(self, imag):
        if not (hasattr(imag, "__int__") or hasattr(imag, "__float__")):
            raise TypeError("value must be a number")
        self._imag = imag

    @property
    def reciprocal(self):
        if (self.real**2 + self.imag**2) == 0:
            raise ZeroDivisionError
        reciprocal = Complex(self.real / (self.real**2 + self.imag**2),
                      -self.imag / (self.real**2 + self.imag**2))
        return reciprocal

    def __neg__(self):
        if not (hasattr(self, "real") or hasattr(self, "imag")):
            raise TypeError ("self should have real and imag")
        #real = -(self.real)
        #imag = -(self.imag)
        return Complex(-self.real, -self.imag)

    def __add__(self, other):
        if not (hasattr(other, "real") or hasattr(other, "imag")):
            raise TypeError ("other should have real and imag")
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not (hasattr(other, "real") or hasattr(other, "imag")):
            raise TypeError ("other should have real and imag")
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not (hasattr(other, "real") or hasattr(other, "imag")):
            raise TypeError("other should have real and imag")
        real = ((self.real * other.real) - (self.imag * other.imag))
        imag = ((self.real * other.imag) + (other.real * self.imag))
        return Complex(real, imag)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not (hasattr(other, "real") or hasattr(other, "imag")):
            raise TypeError ("other should have real and imag")
        if other.real == 0 and other.imag == 0:
            raise ZeroDivisionError
        c1 = Complex(self.real, self.imag)
        c2 = Complex(other.real, other.imag).reciprocal
        return c1 * c2

    def __rtruediv__(self, other):
       return self.reciprocal * other

    def __abs__(self):
        if not (hasattr(self, "real") or hasattr(self, "imag")):
            raise TypeError("should have real and imag")
        return int(math.sqrt(self.real ** 2 + self.imag **2))

    def __eq__(self, other):
        if not (hasattr(other, "real") or hasattr(other, "imag")):
            return False
        return self.real == other.real and self.imag == other.imag

    def __lt__(self, other):
        if not (hasattr(self, "real") or hasattr(self, "imag")):
            raise TypeError("should have real and imag")
        return self.__abs__() < other.__abs__()
