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
# The Actors Style Description:
#
# Similar to the letterbox style, but where the 'things' have
# independent threads of execution.
# 
# - The larger problem is decomposed into 'things' that make sense for
#   the problem domain 
# 
# - Each 'thing' has a queue meant for other \textit{things} to place
#   messages in it
# 
# - Each 'thing' is a capsule of data that exposes only its
#   ability to receive messages via the queue
# 
# - Each 'thing' has its own thread of execution independent of the
#   others.
#
def main():
    pass

if __name__ == "__main__":
    main(sys.argv[1])