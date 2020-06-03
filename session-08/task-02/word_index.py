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

#
# The Quarantine Style Description:
# This style is a variation of "The One" Style, with the following additional constraints:
# 
# - Core program functions have no side effects of any kind, including IO
# 
# - All IO actions must be contained in computation sequences that are
#   clearly separated from the pure functions
# 
# - All sequences that have IO must be called from the main program
# 
#
def main():
    pass

if __name__ == "__main__":
    main(sys.argv[1])