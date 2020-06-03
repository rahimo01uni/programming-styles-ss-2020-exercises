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

#
# The Hollywood Style Description:
#
# - Larger problem is decomposed into entities using some form of
#       abstraction (objects, modules or similar)
# - The entities are never called on directly for actions
#
# - The entities provide interfaces for other entities to be
#  able to register callbacks
#
# - At certain points of the computation, the entities call on the other
#  entities that have registered for callbacks
#
#
def main():
    pass

if __name__ == "__main__":
    main(sys.argv[1])