class WordNode(object):
    def __init__(self, word=None, left=None, right=None):
        self.__right = left
        self.__left = right

        self._word = word
        self._array = []

        self.__parent = None

    def get_word(self):
        return self._word

    def add_tuple(self, tup):
        self._array += [tup]

    def array(self):
        return self._array


    """ BTree functions """
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

    def right(self):
        return self.__right

    def left(self):
        return self.__left

    def set_right(self, nxt):
        self.__right = nxt

    def set_left(self, prev):
        self.__left = prev


    def __cmp__(self, other):
        return cmp(self._word, other.get_word())

    def __str__(self):
        res = "["+self._word+": "
        for pos in self._array:
            res += str(pos)+" "
        res += "]"
        return res
