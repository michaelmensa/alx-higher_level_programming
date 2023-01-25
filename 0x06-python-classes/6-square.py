#!/usr/bin/python3
# 5-square.py by Michael Mensah
'''Defines a square by: (based on 4-square.py)'''


class Square:
    '''Defines a square
        with private instance attribute: size'''

    def __init__(self, size=0, position=(0, 0)):
        '''initializes the square class
            Args: size - reps the size of the square
            Raises: TypeError: if size is not integer
                    ValueError: if size is less than zero
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    @property
    def position(self):
        '''Getter to retrieve position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter to set position
        Position must be a tuple of 2 positive int else
        raise TypeError
        '''
        errmsg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(errmsg)
        elif len(value) != 2:
            raise TypeError(errmsg)
        else:
            for t in value:
                if (t < 0):
                    raise TypeError(errmsg)
                elif type(t) is not int:
                    raise TypeError(errmsg)
        self.__position = value

    def area(self):
        '''Public instance/object method
           Returns the current square area
        '''
        return(self.__size ** 2)

    @property
    def size(self):
        '''Getter to retrieve '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter to set value
            raise TypeError if value is not int
            raise ValueError if value > 0
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        '''prints in stdout the square with the character #'''
        if self.__size != 0:
            for n in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__size + self.__position[0]):
                    if y < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        else:
            print()
