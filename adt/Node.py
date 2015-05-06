class Node():
    def __init__(self, item=None, nxt=None, prev=None):
        self.__data = item
        self.__next = nxt
        self.__prev = prev

        self.__parent = None

    """ Binary Tree Functions """
    def set_parent(self, node):
        self.__parent = node;

    def parent(self):
        return self.__parent

    def remove_child(self, node):
        if self.next() == node:
            self.set_next(None)
            return True
        if self.prev() == node:
            self.set_prev(None)
            return True
        return False

    """ Linked lists Functions (Also used for BTs) """
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def next(self):
        return self.__next

    def prev(self):
        return self.__prev

    def set_next(self, nxt):
        self.__next = nxt

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        res = "[Node: " + str(self.get_data())
        if self.prev():
            res += "\t| prev: " + str(self.prev().get_data())
        if self.next():
            res += "\t| next: " + str(self.next().get_data())
        res += "]"
        return res
