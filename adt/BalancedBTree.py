from Node import *


class BalancedBTree(object):
    def __init__(self):
        self._root = None

    def insert(self, data, node=None):
        if self._root is None:
            self._root = Node(data)
            return
        elif node is None:
            node = self._root

        if data is node.get_data():
            node.get_data().merge(data)
            return

        # TRAVERSING TREE TO FIND PLACE
        # LEFT SIDE
        if data < node.get_data():
            # add as left child
            if node.left() is None:
                node.set_left(Node(data))
                node.left().set_parent(node)
                BalancedBTree.update_bal(node.left())
            else:
                self.insert(data, node.left())
        # RIGHT SIDE
        else:
            if node.right() is None:
                node.set_right(Node(data))
                node.right().set_parent(node)
                BalancedBTree.update_bal(node.right())
            else:
                self.insert(data, node.right())

    @staticmethod
    def update_bal(node, h=0):
        # Set the height
        # TODO si no existeix node fill es posa -1
        node.set_height(h)
        bal = 0
        if node.left():
            bal += node.left().get_height()
        else :
            bal -=1
        if node.right():
            bal -= node.right().get_height()
        else :
            bal-=1
        node.set_balance(bal)

        # If the node has a parent, keep going
        if node.parent():
            BalancedBTree.update_bal(node.parent(), h+1)

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

        while probe:

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
            print node
            self.in_order(node.right())

    @staticmethod
    def test():
        tree = BalancedBTree()
        tree.insert(3)
        tree.insert(2)
        tree.insert(1)
        tree.insert(4)
        tree.insert(5)

        tree.print_tree()


if __name__ == "__main__":
    BalancedBTree.test()