from WordData import *

class Node():
    def __init__(self, data=None, left=None, right=None):

        self.__right = left
        self.__left = right
        self.__data = data

        self.__parent = None

    """ Binary Tree Functions """
    def set_parent(self, node):
        self.__parent = node;

    def parent(self):
        return self.__parent

    def remove_child(self, node):
        if self.right() == node:
            self.set_right(None)
            return True
        if self.left() == node:
            self.set_left(None)
            return True
        return False

    """ Linked lists Functions (Also used for BTs) """
    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def right(self):
        return self.__right

    def left(self):
        return self.__left

    def set_right(self, nxt):
        self.__right = nxt

    def set_left(self, prev):
        self.__left = prev
