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
# The Bulletin Board Style Description:
#
# - Larger problem is decomposed into entities using some form of abstraction
#   (objects, modules or similar)
# 
# - The entities are never called on directly for actions
# 
# - Existence of an infrastructure for publishing and subscribing to
#   events, aka the bulletin board
# 
# - Entities post event subscriptions (aka 'wanted') to the bulletin
#   board and publish events (aka 'offered') to the bulletin board. the
#   bulletin board does all the event management and distribution#
#
def main():
    pass

if __name__ == "__main__":
    main(sys.argv[1])