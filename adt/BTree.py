__author__ = 'Akira'

from WordNode import *

class BTree(object):

    def __init__(self):
        self._root = None

    def insert(self, word, tup=None):
        probe = self._root
        while True:
            if probe is None:
                self._root = WordNode(word)
                self._root.add_tuple(tup)
                return

            # Insertion
            if probe.left() is None and word < probe.get_word():
                probe.set_left(WordNode(word))
                probe.add_tuple(tup)
                probe.left().set_parent(probe)
                return

            if probe.right() is None and word > probe.get_word():
                probe.set_right(WordNode(word))
                probe.add_tuple(tup)
                probe.right().set_parent(probe)
                return

            # Traversal
            if word > probe.get_word():
                probe = probe.right()
            if word <= probe.get_word():
                probe = probe.left()

    def remove(self, node):
            if node.right() is None and node.left() is None:
                node.parent.remove_child(node)

            # TODO Finish remove from tree
            pass

    def contains(self, word):
        probe = self._root
        if probe is None:
            return False

        while probe:
            if word == probe.get_word():
                return probe

            if word < probe.get_word():
                probe = probe.left()
                continue

            if word > probe.get_word():
                probe = probe.right()
        return False


    def find_pos_for_word(self, word):
        """ Returns the node where the word would go. If the node is not found it creates a new one
          and returns that node. """
        probe = self._root

        if probe is None:
            self._root = WordNode(word)
            return self._root

        while probe is not None:

            if word < probe.get_word():
                if probe.left() is None:
                    new_node = WordNode(word)
                    new_node.set_parent(probe)
                    probe.set_left(new_node)
                    return new_node
                else:
                    probe = probe.left()
                    continue

            if word > probe.get_word():
                if probe.right() is None:
                    new_node = WordNode(word)
                    new_node.set_parent(probe)
                    probe.set_right(new_node)
                    return new_node
                else:
                    probe = probe.right()
                    continue

            if word == probe.get_word():
                return probe

    def print_tree(self):
        self.in_order(self._root)

    def in_order(self, node):
        if node:
            self.in_order(node.left())
            print(node.get_word(), node.array())
            self.in_order(node.right())



    @staticmethod
    def test():
        tree = BTree()
        tree.insert("H")
        tree.insert("A", (5, 1))
        tree.insert("Z")
        print tree.contains("Hello")
        print tree.contains("A")

if __name__ == "__main__":
    BTree.test()