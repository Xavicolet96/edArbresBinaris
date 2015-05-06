class Node():
    def __init__(self, item=None, nxt=None, prev=None):
        self.__data = item
        self.__right = nxt
        self.__left = prev

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
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def right(self):
        return self.__right

    def left(self):
        return self.__left

    def set_right(self, nxt):
        self.__right = nxt

    def set_left(self, prev):
        self.__left = prev

    def __str__(self):
        res = "[Node: " + str(self.get_data())
        if self.left():
            res += "\t| prev: " + str(self.left().get_data())
        if self.right():
            res += "\t| next: " + str(self.right().get_data())
        res += "]"
        return res
