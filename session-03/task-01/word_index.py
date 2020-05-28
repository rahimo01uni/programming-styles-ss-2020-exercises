#!/usr/bin/env python
import sys, re, operator, string

# Program Description:
#
# Word Index is a program that takes a plain text file as input and
# outputs all the words contained in it
# sorted alphabetically along with the page numbers on which they occur.
# The program assumes that a page is a
# sequence of 45 lines, each line has max 80 characters, and there is no
# hyphenation. Additionally, Word Index
# must ignore all words that occur more than 100 times.


# Things Style Description:
#
# - The larger problem is decomposed into 'things' that make sense for
#   the problem domain
#
# - Each 'thing' is a capsule of data that exposes procedures to the
#   rest of the world
#
# - Data is never accessed directly, only through these procedures
#
# - Capsules can reappropriate procedures defined in other capsules


# Q1: Would defining a GLOBAL constant be a violation?
# Q2: How could we manage common configurations?
class DataStorageManager():
    """ Models the contents of the file """

    # Cursor. Arrays start at 0 but lines on a page start at 1
    _currentLine = 0

    def __init__(self, path_to_file):
        with open(path_to_file) as f:
            self._data = f.read()
        self._lines = self._data.split('\n')
        pattern = re.compile('[\W_]+')
        for idx in range(len(self._lines)):
            self._lines[idx] = pattern.sub(' ', self._lines[idx]).lower()

    def has_next_line(self):
        return self._currentLine < len(self._lines) - 1

    def next_line(self):
        """ Return the words in the line or raise an exception """
        self._currentLine += 1
        return self._currentLine, self._lines[self._currentLine - 1].split()


class WordFrequencyManager():
    def __init__(self):
        self._word_freqs = {}

    def increment_count(self, word, page):
        if word in self._word_freqs:
            self._word_freqs[word][1].append(page)
            self._word_freqs[word] = (self._word_freqs[word][0] + 1, list(set(self._word_freqs[word][1])))
        else:
            self._word_freqs[word] = (1, [page])

    def filter_and_sort(self):
        self._word_freqs = {k: v for k, v in self._word_freqs.items() if v[0] <= 100}
        return sorted(self._word_freqs.items())


class WordFrequencyController():
    def __init__(self, path_to_file):
        self._storage_manager = DataStorageManager(path_to_file)
        self._word_freq_manager = WordFrequencyManager()

    def run(self):
        while self._storage_manager.has_next_line():
            line_number, words = self._storage_manager.next_line()
            page_number = int(line_number / 45) +1
            for word in words:
                self._word_freq_manager.increment_count(word, page_number)

        word_freqs = self._word_freq_manager.filter_and_sort()
        for tf in word_freqs:
            print(tf[0], '-', str(tf[1][1])[1:-1])


def main(file_path):
    WordFrequencyController(file_path).run()


if __name__ == "__main__":
    main(sys.argv[1])