#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            number_of_instances (int): number of instances
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        area = self.__width*self.__height
        return (area)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        perimeter = self.__width*2 + self.height*2
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return (perimeter)

    def __str__(self):
        """return a rectangle"""
        aux = ''
        if self.width == 0 or self.height == 0:
            return (aux)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    aux = aux + str(self.print_symbol)
                if (i + 1) < self.__height:
                    aux = aux + '\n'
            return aux

    def __repr__(self):
        """return a string representation of the rectangle"""
        a = "Rectangle(" + str(self.__width)
        a = a + ", " + str(self.__height)
        a = a + ")"
        return a

    def __del__(self):
        """Delete an instance of Rectangle"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)
