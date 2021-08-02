from ..src.Figures.Triangle import Triangle
from ..src.Figures.Rectangle import Rectangle
from ..src.Figures.Square import Square
from ..src.Figures.Circle import Circle
import pytest

def area_or_perimetr_compute(*args, **kwargs):

    '''
    Данная функция определяет количество переданных ей в args параметров и в соответствии
    с их количеством создает объект требуемой геометрической фигуры. Далее в зависимости от значения
    параметров, переданных в kwargs, возвращает либо значение площади соданной фигуры либо её периметра

    :param args: параметры геометрической фигуры
    :param kwargs: значение вычисляемой характеристики фигуры (периметр или площадь)
    :return: значение периметра или площади фигуры
    '''

    if isinstance(*args, int):
        a = args[0]
        figure_obj = Square(a)

    elif 'radius' in args[0]:
        radius_value = args[0]['radius']
        figure_obj = Circle(radius_value)

    elif len(*args) == 2:
        a,b = args[0]
        figure_obj = Rectangle(a,b)

    elif len(*args) == 3:
        a,b,c = args[0]
        figure_obj = Triangle(a,b,c)

    if 'area' in kwargs.keys():
        required_parametr = figure_obj.area

    elif 'perimetr' in kwargs.keys():
        required_parametr = figure_obj.perimetr

    return required_parametr

class TestAreaPerimetrCalculation():

    @pytest.mark.parametrize("figure_sizes,expected_value",[((10,8,15),33),((5,8),26),({'radius':10}, 62.8),(5,20)])
    def test_calculate_perimetr(self,figure_sizes, expected_value):
        assert area_or_perimetr_compute(figure_sizes, perimetr=True) == expected_value

    @pytest.mark.parametrize("figure_sizes,expected_value",[((10,8,15),37),((5,8),80),({'radius':10}, 314.2),(5,25)])
    def test_calculate_area(self, figure_sizes, expected_value):
        assert area_or_perimetr_compute(figure_sizes, area=True) == expected_value

class TestSpecialMethods():

    def test_add_area_method(self):
        triangle = Triangle(9,7,10)
        circle = Circle(8)
        print(triangle.area, circle.area)
        sum_of_areas = triangle.add_area(circle)
        assert sum_of_areas == 232.1

    def test_triangle_validation(self):
        fake_triangle = Triangle(10,20,30)
        assert fake_triangle == None