from ..Figures.Figure import Figure

class Square(Figure):

    def __init__(self, a):
        super(Square, self).__init__(name='Square')
        self._a = a

    def compute_perimetr(self):
        self._perimetr = 4*self._a

    def compute_area(self):
        s = self._a**2
        self._area = s

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self.restore_area_and_perimetr()
        self.validate_side(value)
        self._a = value