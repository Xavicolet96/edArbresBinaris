from Node import *


class BalancedBTree(object):
    def __init__(self):
        self._root = None

    def get_root(self):
        return self._root

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
        else:
            bal += 1

        if node.right():
            bal -= node.right().get_height()
        else:
            bal -= 1
        node.set_balance(bal)

        # If the node has a parent, keep going
        if node.parent():
            BalancedBTree.update_bal(node.parent(), h + 1)

    def contains(self, data):
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

    def rotate(self, E, C):
        print "rotating: (%s) by (%s)" % (E.get_data(), C.get_data())

        root = None
        if E.parent():
            root = E.parent()

        if C is E.left():
            E.set_left(None)
        else:
            E.set_right(None)
        C.set_parent(None)

        if C.left() and C.left().get_height() == 0:
            C.left().set_parent(E)
            E.set_right(C.left())
            C.set_left(None)
        else:
            C.right().set_parent(E)
            E.set_left(C.right())
            C.set_right(None)

        # Node arrel
        E.set_parent(C)
        if C.left() is None:
            C.set_left(E)
        else:
            C.set_right(E)

        # Arreglar Root
        if root:
            C.set_parent(root)
            if root.left() is E:
                root.set_left(C)
            else:
                root.set_right(C)
        if E is self._root:
            self._root = C

        self.refresh_tree(self._root)

    def balance_tree(self):


    @staticmethod
    def refresh_tree(node):
        """ call update_bal on all leaves """
        if node.left():
            BalancedBTree.refresh_tree(node.left())
        if node.right():
            BalancedBTree.refresh_tree(node.right())
        if not node.left() and not node.right():
            BalancedBTree.update_bal(node)

    @staticmethod
    def test():
        tree = BalancedBTree()
        tree.insert("E")
        tree.insert("C")
        tree.insert("F")
        tree.insert("B")
        tree.insert("D")
        tree.insert("A")

        nodes = []
        c = ord("A")
        for n in range(6):
            nodes += [tree.contains(chr(c+n))]

        tree.print_tree()

        E = tree.contains("E")
        C = tree.contains("C")


        print "\nFinal tree:"
        #BalancedBTree.refresh_tree(tree.get_root())
        tree.print_tree()


if __name__ == "__main__":
    BalancedBTree.test()