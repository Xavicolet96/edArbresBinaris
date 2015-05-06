__author__ = 'Akira'

from Node import *

class BinarySearchTree(object):

    def __init__(self):
        self._root = None

    def insert(self, item):
        # TODO Rotate functions to keep the tree balanced
        probe = self._root
        while True:
            print "inserting"
            if probe is None:
                self._root = Node(item)
                return

            # Insertion
            if probe.left() is None and item < probe.get_data():
                probe.set_right(Node(item))
                probe.left().set_parent(probe)
                return
            if probe.right() is None and item > probe.get_data():
                probe.set_right(Node(item))
                probe.right().set_parent(probe)
                return

            # Traversal
            if item > probe.get_data():
                probe = probe.right()
            if item < probe.get_data():
                probe = probe.left()

    def remove(self, node):
            if node.right() is None and node.left() is None:
                node.parent.remove_child(node)

            # TODO Finish remove from tree
            pass


    def contains(self, item, node=None):
        """ Recursive function that returns True if the tree contains the given item. """
        if self._root is None:
            return False

        if node is None:
            node = self._root

        if node.get_data() == item:
            return True

        elif item < node.get_data() and node.left() is None:
            return self.contains(node.left, item)

        elif item > node.get_data() and node.right() is None:
            return self.contins(node.right, item)

        return False

    def __str__(self):
        if self._root is None:
            return "[Empty Tree]"
        node = self._root

        res = str(node) + self._get_str(node.left()) + self._get_str(node.right())
        return res


    def _get_str(self, node):
        # TODO Define a recursive method to get a string from a tree of nodes
        pass

    @staticmethod
    def test():
        tree = BinarySearchTree()
        tree.insert("H")
        tree.insert("A")
        tree.insert("Z")
        print tree.contains("Hello")

        print tree

if __name__ == "__main__":
    BinarySearchTree.test()