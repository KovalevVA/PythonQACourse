from math import sqrt
from ..Figures.Figure import Figure

class Triangle(Figure):

    @classmethod
    def check_triangle(self,a,b,c):
        if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
            if a + b > c and b + c > a and c + a > b:
                is_triangle = True
            else:
                is_triangle = False
            return is_triangle
        else:
            raise ValueError('Sides of triangle should have int value')

    def __new__(cls, *args):
        if cls.check_triangle(*args):
            return super().__new__(cls)

    def __init__(self, a, b, c):
        super(Triangle, self).__init__(name='Triangle')
        self._a = a
        self._b = b
        self._c = c

    def compute_perimetr(self):
        self._perimetr = round(self._a + self._b + self._c)

    def compute_area(self):
        if self._perimetr == None:
            self.compute_perimetr()
        half_perimetr = self._perimetr/2
        #Вычисление площади треугольника по формуле Герона:
        s = sqrt((half_perimetr*(half_perimetr - self._a)*(half_perimetr - self._b)*(half_perimetr - self._c)))
        self._area = round(s)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @a.setter
    def a(self, value):
        self.restore_area_and_perimetr()
        self.validate_side(value)
        self._a = value

    @b.setter
    def b(self, value):
        self.restore_area_and_perimetr()
        self.validate_side(value)
        self._b = value

    @c.setter
    def c(self, value):
        self.restore_area_and_perimetr()
        self.validate_side(value)
        self._c = value