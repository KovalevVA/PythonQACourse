from ..Figures.Figure import Figure

class Rectangle(Figure):

    def __init__(self, a, b):
        super(Rectangle, self).__init__(name='Rectangle')
        self._a = a
        self._b = b

    def compute_perimetr(self):
        self._perimetr = 2*(self._a + self._b)

    def compute_area(self):
        s = 2*self._a*self._b
        self._area = s

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

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