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
# The One Description:
#
# - Existence of an abstraction to which values can be
# converted. 
# 
# - This abstraction provides operations to (1) wrap
#   around values, so that they become the abstraction; (2) bind
#   itself to functions, so to establish sequences of functions;
#   and (3) unwrap the value, so to examine the final result.
# 
# - Larger problem is solved as a pipeline of functions bound
#   together, with unwrapping happening at the end.
# 
# - Particularly for The One style, the bind operation simply
#   calls the given function, giving it the value that it holds, and holds
#   on to the returned value.
#
def main():
    pass

if __name__ == "__main__":
    main(sys.argv[1])