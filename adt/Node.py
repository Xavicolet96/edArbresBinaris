class Node():
    def __init__(self, word=None, left=None, right=None):
        self.__word = word
        self.__array = []
        self.__right = left
        self.__left = right

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
    def set_word(self, word):
        self.__word = word

    def get_word(self):
        return self.__word

    def array(self):
        return self.__array

    def add_tuple(self, tup):
        self.__array += [tup]

    def right(self):
        return self.__right

    def left(self):
        return self.__left

    def set_right(self, nxt):
        self.__right = nxt

    def set_left(self, prev):
        self.__left = prev

    def __cmp__(self, other):
        return cmp(self.get_word(), other.get_word())

    def __str__(self):
        res = "[Node: " + str(self.get_word())
        if self.left():
            res += "\t| prev: " + str(self.left().get_word())
        if self.right():
            res += "\t| next: " + str(self.right().get_word())
        res += "]"
        return res
