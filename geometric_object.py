import math


class GeometricObject:
    """
    Class representing geometric object
    """

    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        """
        Sets all the necessary attributes for the class GeometricObject
        :param x:
        :param y:
        :param color:
        :param filled:
        """

        if isinstance(x, int | float):
            self.__x = float(x)
        else:
            self.__x = 0.0

        if isinstance(y, int | float):
            self.__y = float(y)
        else:
            self.__y = 0.0

        if isinstance(color, str):
            self.color = color
        else:
            self.color = 'black'

        if isinstance(filled, bool):
            self.filled = filled
        else:
            self.filled = False

    def set_coordinate(self, new_x, new_y):
        """
        Method of setting coordinates
        :param new_x:
        :param new_y:
        :return:
        """

        if isinstance(new_x, int | float):
            self.__x = float(new_x)
        else:
            self.__x = 0.0

        if isinstance(new_y, int | float):
            self.__y = float(new_y)
        else:
            self.__y = 0.0

    def set_color(self, new_color):
        """
        Method of setting color
        :param new_color:
        :return:
        """

        if isinstance(new_color, str):
            self.color = new_color
        else:
            self.color = 'black'

    def set_filled(self, new_filled):
        """
        Method of setting fill status
        :param new_filled:
        :return:
        """

        if isinstance(new_filled, bool):
            self.filled = new_filled
        else:
            self.filled = False

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

    def __str__(self):
        """
        Method of presenting data for printing data of class GeometricObject
        :return:
        """

        return f'({self.get_x()}, {self.get_y()})\n' \
               f'color: {self.get_color()}\n' \
               f'filled: {self.is_filled()}\n'

    def __repr__(self):
        """
        Method of representing data of class GeometricObject
        :return:
        """

        if self.is_filled():
            status = ''
        else:
            status = 'no '

        return f'({int(self.get_x())},{int(self.get_y())})' \
               f' {self.get_color()} {status}filled'


class Rectangle(GeometricObject):
    """
    Class representin rectangle
    """

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0,
                 color='black', filled=False):
        """
        Sets all the necessary attributes for the class Rectangle
        :param x:
        :param y:
        :param width:
        :param height:
        :param color:
        :param filled:
        """

        super().__init__(x, y, color, filled)

        if isinstance(width, int | float) and width > 0:
            self.width = float(width)
        else:
            self.width = 0.0

        if isinstance(height, int | float) and height > 0:
            self.height = float(height)
        else:
            self.height = 0.0

    def set_width(self, new_width):
        if isinstance(new_width, int | float) and new_width > 0:
            self.width = float(new_width)
        else:
            self.width = 0.0

    def set_height(self, new_height):
        if isinstance(new_height, int | float) and new_height > 0:
            self.height = float(new_height)
        else:
            self.height = 0.0

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        """
        Method of getting the area of the rectangle
        :return:
        """

        return self.width * self.height

    def get_perimetr(self):
        """
        Method of getting the perimetr of the rectangle
        :return:
        """

        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Method of presenting data for printing data of class Rectangle
        :return:
        """

        return f'width: {self.get_width()}\n' \
               f'height: {self.get_height()}\n'\
               f'({self.get_x()}, {self.get_y()})\n' \
               f'color: {self.get_color()}\n' \
               f'filled: {self.is_filled()}\n'

    def __repr__(self):
        """
        Method of representing data of class Rectangle
        :return:
        """

        if self.is_filled():
            status = ''
        else:
            status = 'no '

        return f'width:{int(self.get_width())}, height:{int(self.get_height())}' \
               f' ({int(self.get_x())},{int(self.get_y())}) {self.get_color()}' \
               f' {status}filled'


class Circle(GeometricObject):

    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        """
        Sets all the necessary attributes for the class Circle
        :param x:
        :param y:
        :param radius:
        :param color:
        :param filled:
        """

        super().__init__(x, y, color, filled)
        if isinstance(radius, int | float) and radius > 0:
            self.__radius = float(radius)
        else:
            self.__radius = 0.0

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, int | float) and value > 0:
            self.__radius = float(value)
        else:
            self.__radius = 0.0

    def get_area(self):
        """
        Method of getting the area of the circle
        :return:
        """

        return math.pi * self.radius ** 2

    def get_perimetr(self):
        """
        Method of getting the perimetr of the circle
        :return:
        """

        return 2 * math.pi * self.radius

    def get_diametr(self):
        """
        Method of getting the diameter of the circle
        :return:
        """

        return 2 * self.radius

    def __str__(self):
        """
        Method of presenting data for printing data of class Circle
        :return:
        """

        return f'radius: {self.radius}\n'\
               f'({self.get_x()}, {self.get_y()})\n' \
               f'color: {self.get_color()}\n' \
               f'filled: {self.is_filled()}\n'

    def __repr__(self):
        """
        Method of representing data of class Circle
        :return:
        """

        if self.is_filled():
            status = ''
        else:
            status = 'no '

        return f'radius:{int(self.radius)} ({int(self.get_x())},' \
               f'{int(self.get_y())}) {self.get_color()} {status}filled'
