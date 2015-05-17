from Node import *


class BalancedBTree(object):
    def __init__(self):
        self._root = None

    def get_root(self):
        return self._root

    def insert(self, data):
        """ Method visible from outside """
        if self._root is None:
            self._root = Node(data)
            return

        self._insert(data, self._root)

    def _insert(self, data, node):
        """ The recursive insertion method """
        if data == node.get_data():
            node.get_data().merge(data)
            return

        # TRAVERSING TREE TO FIND PLACE
        # LEFT SIDE
        if data < node.get_data():
            # add as left child
            if node.left() is None:
                node.set_left(Node(data))
                node.left().set_parent(node)
                self.update_bal(node.left())

                self.balance_tree(node)

            else:
                self._insert(data, node.left())
        # RIGHT SIDE
        else:
            if node.right() is None:
                node.set_right(Node(data))
                node.right().set_parent(node)
                self.update_bal(node.right())

                self.balance_tree(node)

            else:
                self._insert(data, node.right())

    def update_bal(self, node, h=0):
        """ Runs up the tree updating the balance and height of each node"""
        node.set_height(max(h, node.get_height()))
        bal = 0
        if node.left():
            bal += node.left().get_height()
        else:
            bal -= 1

        if node.right():
            bal -= node.right().get_height()
        else:
            bal += 1
        node.set_balance(bal)

        # If the node has a parent, keep going
        if node.parent():
            self.update_bal(node.parent(), h + 1)

    def balance_tree(self, node):
        """ Runs up the tree from a given node, checking if any node is imbalanced, if so, rotates it. """

        if abs(node.get_balance()) > 1:
            if node.get_balance() > 0:
                self.rotate(node, node.left(), "right")
                return
            else:
                self.rotate(node, node.right(), "left")
                return

        if node.parent():
            self.balance_tree(node.parent())

    def contains(self, word):
        """ Returns the node if word is found, otherwise returns False """
        probe = self._root
        if probe is None:
            return False

        while probe:
            if word == probe.get_data().word():
                return probe

            if word < probe.get_data().word():
                probe = probe.left()
                continue

            if word > probe.get_data().word():
                probe = probe.right()
        return False

    def print_tree(self):
        def prt(n):
            print n
        """ Print the tree following the in_order sequence """
        self.for_in_order_do(self._root, prt)


    def reset_heights(self):
        """ Sets thhe height for every node to zero before updating height and balance """
        def h2zero(n):
            n.set_height(0)
        self.for_in_order_do(self._root, h2zero)

    def for_in_order_do(self, node, f):
        """ Runs a function on all nodes from node downwards following the in_order sequence"""
        if node:
            self.for_in_order_do(node.left(), f)
            f(node)
            self.for_in_order_do(node.right(), f)

    def rotate(self, root, pivot, side):
        # STEP 0
        # Connect the rest of the tree to the Pivot node
        pivot.set_parent(root.parent())
        if root.parent():
            if root.is_left():
                root.parent().set_left(pivot)
            elif root.is_right():
                root.parent().set_right(pivot)

        # rotate the given side
        if side is "left":
            self.rotate_left(root, pivot)
        elif side is "right":
            self.rotate_right(root, pivot)

        # Check for root pointer redirection
        if root is self._root:
            self._root = pivot

        # Update the tree balance factors and height afterwards
        self.refresh_tree()

    @staticmethod
    def rotate_left(root, pivot):
        # STEP 1
        root.set_right(pivot.left())
        if pivot.left():
            pivot.left().set_parent(root)
        # STEP 2
        pivot.set_left(root)
        root.set_parent(pivot)

    @staticmethod
    def rotate_right(root, pivot):
        # STEP 1
        root.set_left(pivot.right())
        if pivot.right():
            pivot.right().set_parent(root)
        # STEP 2
        pivot.set_right(root)
        root.set_parent(pivot)

    def refresh_tree(self):
        self.reset_heights()
        self._refresh_tree(self._root)

    def _refresh_tree(self, node):
        """ call update_bal on all leaves """
        if node.left():
            self._refresh_tree(node.left())
        if node.right():
            self._refresh_tree(node.right())
        if not node.left() and not node.right():
            self.update_bal(node)

    @staticmethod
    def test():
        tree = BalancedBTree()

        tree.insert("A")
        tree.insert("B")
        tree.insert("C")
        tree.insert("D")
        tree.insert("E")
        tree.insert("F")

        tree.print_tree()


if __name__ == "__main__":
    BalancedBTree.test()