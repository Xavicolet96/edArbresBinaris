__author__ = 'Akira'

from Node import *

class BalancedBTree(object):

    def __init__(self):
        self._root = None

    # TODO Finish insert method for BalancedTree
    def insert(self, node, word, tup = None):
        if node.get_word() is word:
            # data already in tree
            return

        # TRAVERSING TREE TO FIND NODE
        if word < node.get_word():
            # add as left child
            if node.left is None:
                # node.set_left(toInsert)
                pass
            else:
                # insert(node.left, toInsert)
                update_bal(node.left())

        elif node.right is None:
                pass
                # add as right child
                # node.addRight(toInsert)
        else:
            self.insert(node.right,	word, tup)
            update_bal(node.right())

    def old_insert(self, word, tup=None):
        # TODO Rotate functions to keep the tree balanced
        probe = self._root
        while True:
            if probe is None:
                self._root = Node(word)
                self._root.add_tuple(tup)
                return

            # Insertion
            if probe.left() is None and word < probe.get_word():
                probe.set_right(Node(word))
                probe.add_tuple(tup)
                probe.left().set_parent(probe)
                return

            if probe.right() is None and word > probe.get_word():
                probe.set_right(Node(word))
                probe.add_tuple(tup)
                probe.right().set_parent(probe)
                return

            # Traversal
            if word > probe.get_word():
                probe = probe.right()
            if word <= probe.get_word():
                probe = probe.left()

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
            self._root = Node(word)
            return self._root

        while probe is not None:

            if word < probe.get_word():
                if probe.left() is None:
                    new_node = Node(word)
                    new_node.set_parent(probe)
                    probe.set_left(new_node)
                    return new_node
                else:
                    probe = probe.left()
                    continue

            if word > probe.get_word():
                if probe.right() is None:
                    new_node = Node(word)
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
        tree = BalancedBTree()
        tree.insert("H")
        tree.insert("A")
        tree.insert("Z")
        print tree.contains("Hello")
        print tree.contains("A")

# TODO Create update_bal function for BalanedBTREE
def update_bal(node):
        pass

if __name__ == "__main__":
    BalancedBTree.test()