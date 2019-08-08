# -*- coding: utf-8 -*-
"""
@author: Liu Hongzhi

Email: Kimlau0811@gmail.com

Created on Thu Aug  8 12:23:52 2019
"""

class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy