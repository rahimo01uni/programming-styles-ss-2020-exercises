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
# The Kick-forward Style Description:
#
# Variation of the pipeline style, with the following additional constraints:
# 
# - Each function takes an additional parameter, usually the 
#   last, which is another function
# 
# - That function parameter is applied at the end of the current
#   function
# 
# - That function parameter is given as input what would be the
#   output of the current function
# 
# - Larger problem is solved as a pipeline of functions, but where
#   the next function to be applied is given as parameter to the current function
#
def main():
    pass

if __name__ == "__main__":
    main(sys.argv[1])