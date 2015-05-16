class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.__right = left
        self.__left = right
        self.__data = data

        self._height = 0
        self._balance = 0
        self._parent = None

    def __str__(self):
        lft = ""
        rght = ""
        prt = ""
        if self.left():
            lft = self.left().get_data()
        if self.right():
            rght = self.right().get_data()
        if self.parent():
            prt = self.parent().get_data()
        return "%6s | (P:%2s)(L:%2s)(R:%2s) | H:%2d B:%2d" % (str(self.__data), prt, lft, rght, self._height, self._balance)

    """ Binary Tree Functions """
    def set_parent(self, node):
        self._parent = node

    def parent(self):
        return self._parent

    def get_height(self):
        return self._height

    def set_height(self, h):
        self._height = h

    def get_balance(self):
        return self._balance

    def set_balance(self, b):
        self._balance = b

    def remove_child(self, node):
        if self.right() == node:
            self.set_right(None)
            return True
        if self.left() == node:
            self.set_left(None)
            return True
        return False

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
