#!/usr/bin/env python

# Program Description:
#
# Word Index is a program that takes a plain text file as input and
# outputs all the words contained in it
# sorted alphabetically along with the page numbers on which they occur.
# The program assumes that a page is a
# sequence of 45 lines, each line has max 80 characters, and there is no
# hyphenation. Additionally, Word Index
# must ignore all words that occur more than 100 times.


# Cookbook Style Description:
#   - Larger problem decomposed in procedural abstractions
#   - Larger problem solved as a sequence of commands, each corresponding to a procedure


# Global Constants:
#   Q1: Do the constants violate the style?
LINES_PER_PAGE = 45
MAX_SIZE_LINE = 80
STOP_FREQUENCY_LIMIT = 100


def main(file_path):
    raise Error("Not Yet implemented")

if __name__ == "__main__":
    main(sys.argv[1])