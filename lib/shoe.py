#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def brand(self):
        """The brand property"""
        return self._brand

    @brand.setter
    def brand(self, brand):
        """The brand setter"""
        self._brand = brand

    @property
    def size(self):
        """The size property"""
        return self._size

    @size.setter
    def size(self, size):
        """size must be an integer"""
        if(type(size) == int):
            self._size = size
        else:
            print("size must be an integer")

    @property
    def condition(self):
        """The condition property"""
        return self._condition

    @condition.setter
    def condition(self, condition):
        """The condition setter"""
        self._condition = condition
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")