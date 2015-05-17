__author__ = 'xavier'

from adt.BalancedBTree import *
from adt.WordData import *
from time import clock


class BalancedBTreeWordFinder:
    def __init__(self):
        self._tree = BalancedBTree()

    def main(self):
        t0 = clock()
        self.append_text("largeText.txt")
        t1 = clock()
        print "\nInsertion time: %.2fs" % (t1 - t0)

        t0 = clock()
        f = open("dictionary.txt", "r")
        for line in f:
            for word in line.split():
                node = self._tree.contains(word.lower())
                if node is not False:
                    print "%s at: %s" % (node.get_data().word(), node.get_data().pos())
        f.close()
        t1 = clock()

        print "\nSearch time: %.2fs" % (t1 - t0)

    def test(self):
        self.append_text("smallText.txt")

        def print_node(n):
            print "%s at: %s" % (n.get_data().word(), n.get_data().pos())

        self._tree.for_in_order_do(self._tree.get_root(), print_node)

    def append_text(self, filename):
        line_n = 0
        pos = 0

        with open(filename, 'r') as f:
            for line in f:
                # line = re.sub(r'\W+', '', line)
                # print line

                # For each line, insert each separate word in the tree
                pos = 0
                for word in line.split():
                    self.insert_word(word.lower(), line_n, pos)
                    pos += 1
                line_n += 1
            f.close()

    def insert_word(self, word, line, pos):
        # print "'%s' \t\t line: %s pos: %s" % (word, line, pos)
        data = WordData(word)
        data.add_pos((line, pos))

        self._tree.insert(data)

    def get_tree(self):
        return self._tree

    def find_occurrences(self, word):
        node = self._tree.contains(word)
        if node is not False:
            return node
        return None


    def view_index(self):
        self._tree.print_tree()

        # TODO calcular a profunditat de l'arbre

    def prof(self):
        pass


def main():
    finder = BalancedBTreeWordFinder()
    finder.main()


if __name__ == "__main__":
    main()