__author__ = 'Akira'


class WordData(object):
    def __init__(self, word=None):
        self._positions = []
        self._word = word

    def set_word(self, word):
        self._word = word

    def word(self):
        return self._word

    def add_pos(self, pos):
        self._positions += [pos]

    def pos(self):
        return self._positions

    def merge(self, other):
        """ Merges this WordData with another wordData, adding the positions to this data's list """
        if self._word != other.word():
            print self.word(), other.word()
            raise RuntimeError("Word is not a match for merge.")

        for pos in other.pos():
            self.add_pos(pos)

    def __cmp__(self, other):
        return cmp(self._word, other.word())
