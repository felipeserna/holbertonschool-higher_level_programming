#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <width>"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y,
                       self.width))

    @property
    def size(self):
        """retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """*args: assigns an argument to each attribute
        **kwargs: assigns a key/value argument to attributes
        """
        if args:

            attributes = ['id', 'size', 'x', 'y']
            for count, item in enumerate(args):
                if count < 4:
                    setattr(self, attributes[count], item)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
