from ..Figures.Figure import Figure
from math import pi

class Circle(Figure):

    def __init__(self, r):
        super(Circle, self).__init__(name='Circle')
        self._r = r

    def compute_perimetr(self):
        self._perimetr = round(2*pi*self._r, 1)

    def compute_area(self):
        s = pi*self._r**2
        self._area = round(s,1)

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, value):
        self.restore_area_and_perimetr()
        self.validate_side(value)
        self._r = value