__author__ = 'Akira'

from adt.BTree import *
import re
from time import clock

class BTreeWordFinder:

    def __init__(self):
        self._tree = BTree()

    def main(self):
        self.append_text("smallText.txt")

        f = open("dictionary.txt", "r")
        for line in f:
            for word in line.split():
                arr = self.find_ocurrences(word.lower())
                if arr:
                    print word.lower(), ": posicions: ", arr
        f.close()



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
        #print "'%s' \t\t line: %s pos: %s" % (word, line, pos)
        tup = (line, pos)

        node = self._tree.find_pos_for_word(word)
        node.add_tuple(tup)

    def get_tree(self):
        return self._tree

    def find_ocurrences(self, word):
        node = self._tree.find_pos_for_word(word)
        arr = node.array()
        if len(arr) == 0:
            if node.parent():
                node.parent().remove_child(node)
            return None
        else:
            print "found ", word
            return node.array()


    def view_index(self):
        self._tree.print_tree()


def main():
    finder = BTreeWordFinder()
    finder.main()

if __name__ == "__main__":
    main()