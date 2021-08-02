class Figure(object):

    def __new__(cls, *args):
        if cls is Figure:
            #запрещаем создавать инстансы объекта Figure напрямую
            #возможно создавать экземпляры только от классов потомков Figure
            raise TypeError("class Figure can't be instantiated directly please use its descendents")
        return object.__new__(cls)

    def __init__(self, name):
        self._name = name
        self._area = None
        self._perimetr = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError('name of Figure must be non-empty string')

    @property
    def perimetr(self):
        if self._perimetr == None:
            self.compute_perimetr()
        return self._perimetr

    @property
    def area(self):
        if self._area == None:
            self.compute_area()
        return self._area

    def restore_area_and_perimetr(self):
        self._area = None
        self._perimetr = None

    def validate_side(self, value):
        if isinstance(value, int) and value > 0:
            return value
        else:
            raise ValueError(f'side/radius of {self.name} must be set as non-zero int value')

    def add_area(self, obj):
        if (isinstance(obj.area, int) or isinstance(obj.area, float)) and obj.area > 0:
            return self.area + obj.area
        else:
            raise ValueError(f'area of passed object is not valid, please check the value {obj.area}')