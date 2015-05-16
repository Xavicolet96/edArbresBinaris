from Node import *


class BalancedBTree(object):
    def __init__(self):
        self._root = None

    def get_root(self):
        return self._root

    def insert(self, data):
        print "inserting", data
        """ Method visible from outside """
        if self._root is None:
            self._root = Node(data)
            return

        self._insert(data, self._root)

    def _insert(self, data, node):
        """ The recursive insertion method """
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
        node.set_height(max(h, node.get_height()))
        bal = 0
        if node.left():
            bal += node.left().get_height()
        else:
            bal += 1

        if node.right():
            bal -= node.right().get_height()
        else:
            bal -= 1
        node.set_balance(bal)

        # If the node has a parent, keep going
        if node.parent():
            self.update_bal(node.parent(), h + 1)

    def balance_tree(self, node):
        print "\t> balancing %s" % node.get_data()

        if abs(node.get_balance()) > 1:
            print "node %s is unbalanced" % node
            if node.get_balance() > 0:
                self.rotate(node, node.left())
                return
            else:
                self.rotate(node, node.right())
                return

        if node.parent():
            self.balance_tree(node.parent())

    def contains(self, data):
        """ Returns the node if data is found, otherwise returns False """
        probe = self._root
        if probe is None:
            return False

        while probe:
            if data == probe.get_data():
                return probe

            if data < probe.get_data():
                probe = probe.left()
                continue

            if data > probe.get_data():
                probe = probe.right()
        return False

    def print_tree(self):
        """ Print the tree following the in_order sequence """
        self.for_in_order_do(self._root, quick_print)

    def for_in_order_do(self, node, f):
        """ Runs a function on all nodes from node downwards following the in_order sequence"""
        if node:
            self.for_in_order_do(node.left(), f)
            f(node)
            self.for_in_order_do(node.right(), f)

    def rotate(self, node_e, node_c):
        """ Rotate two nodes """
        print "rotating: (%s) by (%s)" % (node_e.get_data(), node_c.get_data())

        root = None
        if node_e.parent():
            root = node_e.parent()

        if node_c is node_e.left():
            node_e.set_left(None)
        else:
            node_e.set_right(None)
        node_c.set_parent(None)

        if node_c.left() and node_c.left().get_height() == 0:
            node_c.left().set_parent(node_e)
            node_e.set_right(node_c.left())
            node_c.set_left(None)
        else:
            node_c.right().set_parent(node_e)
            node_e.set_left(node_c.right())
            node_c.set_right(None)

        # Node arrel
        node_e.set_parent(node_c)
        if node_c.left() is None:
            node_c.set_left(node_e)
        else:
            node_c.set_right(node_e)

        # Arreglar Root
        if root:
            node_c.set_parent(root)
            if root.left() is node_e:
                root.set_left(node_c)
            else:
                root.set_right(node_c)
        if node_e is self._root:
            self._root = node_c

        self.refresh_tree()

    def refresh_tree(self):
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
        tree.insert("E")
        tree.insert("C")
        tree.insert("B")
        tree.insert("D")
        tree.insert("F")

        tree.print_tree()

        print "\n"

        tree.insert("A")

        print "\n"

        tree.print_tree()

        """
        print "\nFinal tree:"
        tree.print_tree()
        """


def quick_print(string):
    print string

if __name__ == "__main__":
    BalancedBTree.test()